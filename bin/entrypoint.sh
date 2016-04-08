#!/bin/bash

set -e

setup-user.sh "${PROJECT_NAME}" "${PROJECT_DIR}/var"
exec gosu-dir.sh "${PROJECT_DIR}/var" setup-django-env.sh "$@"
