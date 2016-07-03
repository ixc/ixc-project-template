FROM buildpack-deps:jessie

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gettext \
        jq \
        nano \
        postgresql-client \
        python \
        python-dev \
        pv \
    && rm -rf /var/lib/apt/lists/*

ENV NODE_VERSION=4.4.2
RUN wget -nv -O - "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz" | tar -Jx -C /opt/ -f -
RUN ln -s "/opt/node-v${NODE_VERSION}-linux-x64/bin/node" /usr/local/bin/
RUN ln -s "/opt/node-v${NODE_VERSION}-linux-x64/bin/npm" /usr/local/bin/

WORKDIR /opt/{{ project_name }}/

COPY package.json /opt/{{ project_name }}/
RUN npm install && rm -rf /root/.npm
RUN md5sum package.json > package.json.md5
ENV PATH=/opt/{{ project_name }}/node_modules/.bin:$PATH

COPY bower.json /opt/{{ project_name }}/
RUN bower install --allow-root && rm -rf /root/.cache/bower
RUN md5sum bower.json > bower.json.md5

RUN wget -nv -O - https://bootstrap.pypa.io/get-pip.py | python
RUN pip install --no-cache-dir pip-accel[s3]

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ENV PIP_ACCEL_AUTO_INSTALL=no
ENV PIP_ACCEL_CACHE=/root/.pip-accel
ENV PIP_ACCEL_S3_BUCKET=ixc-pip-accel
ENV PIP_ACCEL_S3_PREFIX=docker-buildpack-deps-jessie
ENV PIP_ACCEL_TRUST_MOD_TIMES=no

ARG PIP_INDEX_URL=https://devpi.ixcsandbox.com/ic/dev/+simple
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_INDEX_URL=$PIP_INDEX_URL

COPY requirements*.txt /opt/{{ project_name }}/
RUN pip-accel install -r requirements.txt && rm -rf $PIP_ACCEL_CACHE

COPY setup.py /opt/{{ project_name }}/
RUN pip install --no-cache-dir -e .

RUN md5sum requirements*.txt setup.py > venv.md5

ENV DOCKERIZE_VERSION=0.2.0
RUN wget -nv -O - "https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz" | tar -xz -C /usr/local/bin/ -f -

ENV GOSU_VERSION=1.7
RUN wget -nv -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture)"
RUN chmod +x /usr/local/bin/gosu

ENV TINI_VERSION=0.9.0
RUN wget -nv -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static"
RUN chmod +x /usr/local/bin/tini

ENV DOCKER_COMMIT=3000001ff3e0cc024fc81bf089721dd727855052
RUN cd /usr/local/bin \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/bower-install.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/gulp.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/migrate.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/npm-install.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/pip-install.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/setup-postgres.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/supervisor.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/transfer.sh" \
    && chmod +x *.sh

# See: https://github.com/codekitchen/dinghy/issues/17#issuecomment-209545602
RUN echo "int chown() { return 0; }" > preload.c && gcc -shared -o /libpreload.so preload.c && rm preload.c
ENV LD_PRELOAD=/libpreload.so

ENV PATH=/opt/{{ project_name }}/bin:$PATH
ENV PROJECT_DIR=/opt/{{ project_name }}
ENV PROJECT_NAME={{ project_name }}
ENV PYTHONHASHSEED=random
ENV PYTHONWARNINGS=ignore

VOLUME /root
VOLUME /tmp

ENTRYPOINT ["tini", "--", "entrypoint.sh"]
CMD ["migrate.sh", "supervisor.sh"]

COPY . /opt/{{ project_name }}/

RUN python manage.py collectstatic --noinput --verbosity=0
RUN python manage.py compress --verbosity=0
