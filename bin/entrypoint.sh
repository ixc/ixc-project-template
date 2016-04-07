#!/bin/bash

set -e

setup-user.sh "${PROJECT_NAME}" "${PROJECT_DIR}/var"

# Work around inconsistent behaviour with Docker for Mac file sharing.
if [[ $(stat -c '%u' "${PROJECT_DIR}/var") == 0 ]]; then
	exec gosu "${PROJECT_NAME}" entrypoint-django.sh "$@"
fi

exec entrypoint-gosu-dir.sh "${PROJECT_DIR}/var" entrypoint-django.sh "$@"
