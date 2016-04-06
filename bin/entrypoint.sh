#!/bin/bash

set -e

setup-user.sh "${PROJECT_NAME}" "${PROJECT_DIR}/var"
exec entrypoint-gosu-dir.sh "${PROJECT_DIR}/var" entrypoint-django.sh "$@"
