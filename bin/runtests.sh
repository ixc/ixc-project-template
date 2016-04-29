#!/bin/bash

echo "# ${0}"

set -e

export DJANGO_SETTINGS_MODULE={{ project_name }}.tests.settings
export PGDATABASE="test_${PGDATABASE}"
export REUSE_DB=1
export SETUP_POSTGRES_FORCE=1
export SRC_PGDATABASE=/opt/{{ project_name }}/test_{{ project_name }}.sql

setup-postgres.sh
python manage.py migrate --noinput
python manage.py test -v 2 --noinput "$@"
