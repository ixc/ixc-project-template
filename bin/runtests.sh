#!/bin/bash

cat <<'EOF'

#
# runtests.sh [options]
#
# Setup environment for test project and run the `test` management command.

EOF

set -e

export DJANGO_SETTINGS_MODULE={{ project_name }}.tests.settings
export PGDATABASE="test_${PGDATABASE}"
export REUSE_DB=1
export SETUP_POSTGRES_FORCE=1
export SRC_PGDATABASE=/opt/{{ project_name }}/test_{{ project_name }}.sql

setup-postgres.sh

python manage.py migrate --noinput

coverage run manage.py test -v 2 --noinput {{ project_name }} "$@"
coverage report
