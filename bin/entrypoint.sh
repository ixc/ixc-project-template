#!/bin/bash

cat <<EOF

#
# `whoami`@`hostname`:$PWD$ entrypoint.sh $@
#
# Setup environment for Django and local development, setup PostgreSQL database,
# and execute command as unprivileged user.
#

EOF

set -e

exec gosu-dir.sh /opt/{{ project_name }}/var setup-django-env.sh setup-local-env.sh setup-postgres.sh "$@"
