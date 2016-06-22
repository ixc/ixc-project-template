FROM buildpack-deps:jessie

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        jq \
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
RUN npm install
ENV PATH=/opt/{{ project_name }}/node_modules/.bin:$PATH

COPY bower.json /opt/{{ project_name }}/
RUN bower install --allow-root

RUN wget -nv -O - https://bootstrap.pypa.io/get-pip.py | python
RUN pip install --no-cache-dir pip-accel[s3]

ARG AWS_ACCESS_KEY_ID=AKIAIGZZ2KQ4PBOI3RHA
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID

ARG AWS_SECRET_ACCESS_KEY

ENV PIP_ACCEL_CONFIG=/opt/{{ project_name }}/pip-accel.conf

ARG PIP_INDEX_URL=https://devpi.ixcsandbox.com/ic/dev/+simple
ENV PIP_INDEX_URL=$PIP_INDEX_URL

COPY pip-accel.conf requirements.txt /opt/{{ project_name }}/
RUN pip-accel install -r requirements.txt && rm -rf /var/cache/pip-accel

COPY setup.py /opt/{{ project_name }}/
RUN pip install -e .

ENV DOCKERIZE_VERSION=0.2.0
RUN wget -nv -O - "https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz" | tar -xz -C /usr/local/bin/ -f -

ENV GOSU_VERSION=1.7
RUN wget -nv -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture)"
RUN chmod +x /usr/local/bin/gosu

ENV TINI_VERSION=0.9.0
RUN wget -nv -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static"
RUN chmod +x /usr/local/bin/tini

ENV DOCKER_COMMIT=ce3c50df2d8fa5c94b13b15db3d92be93427fd7f
RUN cd /usr/local/bin \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/gosu-dir.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/gulp.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/migrate.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/setup-django-env.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/setup-local-env.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/setup-postgres.sh" \
    && wget -N -nv "https://raw.githubusercontent.com/ixc/docker/${DOCKER_COMMIT}/bin/supervisor.sh" \
    && chmod +x *.sh

RUN adduser --system --home /opt/{{ project_name }}/var/ {{ project_name }}
VOLUME /opt/{{ project_name }}/var/

ENV PATH=/opt/{{ project_name }}/bin:$PATH
ENV PROJECT_DIR=/opt/{{ project_name }}
ENV PROJECT_NAME={{ project_name }}

ENTRYPOINT ["tini", "--", "entrypoint.sh"]
CMD ["migrate.sh", "supervisor.sh"]

COPY . /opt/{{ project_name }}/

ENV PYTHONWARNINGS=ignore

RUN python manage.py collectstatic --noinput --verbosity=0
RUN python manage.py compress
