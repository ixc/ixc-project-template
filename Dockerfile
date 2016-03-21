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
ENV PROJECT_DIR=/opt/$PROJECT_NAME
ENV PATH=$PROJECT_DIR/bin:$PROJECT_DIR/node_modules/.bin:$PATH
WORKDIR $PROJECT_DIR

# Node.js packages.
COPY package.json $PROJECT_DIR
RUN npm install

# Bower components.
COPY bower.json $PROJECT_DIR
RUN bower install --allow-root

# Python packages.
COPY setup.py $PROJECT_DIR
RUN pip install -e . --no-cache-dir

# Source.
COPY . $PROJECT_DIR
