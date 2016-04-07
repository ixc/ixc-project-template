FROM buildpack-deps:jessie

ENV BASE_COMMIT=534e86183d3581b51178b37e97065175f53afcc5
RUN wget -nv -O - "https://raw.githubusercontent.com/ixc/base-docker/${BASE_COMMIT}/bootstrap.sh" | sh -s $BASE_COMMIT

ENV DJANGO_COMMIT=c52e9098e0062553d6c9c5f5d6ef08065d7dcc59
RUN wget -nv -O - "https://raw.githubusercontent.com/ixc/django-docker/${DJANGO_COMMIT}/bootstrap.sh" | sh -s $DJANGO_COMMIT

WORKDIR /opt/{{ project_name }}/

ENV PATH=/opt/{{ project_name }}/node_modules/.bin:$PATH
COPY package.json /opt/{{ project_name }}/
RUN npm install

COPY bower.json /opt/{{ project_name }}/
RUN bower install --allow-root

ARG AWS_ACCESS_KEY_ID=AKIAIGZZ2KQ4PBOI3RHA
ARG AWS_SECRET_ACCESS_KEY
ARG PIP_INDEX_URL=https://devpi.ixcsandbox.com/ic/dev/+simple
ENV PIP_ACCEL_CONFIG=/opt/{{ project_name }}/pip-accel.conf
COPY pip-accel.conf requirements*.txt setup.py /opt/{{ project_name }}/
RUN pip-accel install -r requirements.txt -e . && rm -rf /var/cache/pip-accel

ENV PATH=/opt/{{ project_name }}/bin:$PATH
ENV PROJECT_DIR=/opt/{{ project_name }}
ENV PROJECT_NAME={{ project_name }}

ENTRYPOINT ["entrypoint.sh"]
CMD ["supervisor.sh"]

COPY . /opt/{{ project_name }}/
