#!/bin/bash

set -e

setup-user.sh "${PROJECT_NAME}" "${PROJECT_DIR}/var"

# Work around inconsistent behaviour with Docker for Mac file sharing.
if [[ $(stat -c '%u' "${PROJECT_DIR}/var") == 0 ]]; then
	exec gosu "${PROJECT_NAME}" setup-django-env.sh setup-local-env.sh setup-postgres.sh "$@"
fi

exec gosu-dir.sh "${PROJECT_DIR}/var" setup-django-env.sh setup-local-env.sh setup-postgres.sh "$@"
