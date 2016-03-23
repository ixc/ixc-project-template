FROM interaction/django:latest

# Python packages with build dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python-coverage \
        python-crypto \
        python-lxml \
        python-numpy \
        python-pillow \
        python-psycopg2 \
    && rm -rf /var/lib/apt/lists/*

# Build arguments.
ARG PIP_INDEX_URL=https://devpi.ixcsandbox.com/ic/dev/+simple

# Environment.
ENV PROJECT_NAME={{ project_name }}
ENV PROJECT_DIR=/opt/{{ project_name }}
ENV PATH=/opt/{{ project_name }}/bin:/opt/{{ project_name }}/node_modules/.bin:$PATH
WORKDIR /opt/{{ project_name }}/

# Node.js packages.
COPY package.json /opt/{{ project_name }}/
RUN npm install

# Bower components.
COPY bower.json /opt/{{ project_name }}/
RUN bower install --allow-root

# Python packages.
COPY setup.py /opt/{{ project_name }}/
RUN pip install -e . --no-cache-dir

# Source.
COPY . /opt/{{ project_name }}/
