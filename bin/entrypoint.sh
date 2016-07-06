#!/bin/bash

cat <<EOF

#
# `whoami`@`hostname`:$PWD$ entrypoint.sh $@
#
# Setup environment for Django, install NPM packages, Bower components, Python
# packages, setup PostgreSQL database, and execute command.
#

EOF

set -e

mkdir -p var

if [[ -d /opt/.ssh ]]; then
	cp -R /opt/.ssh /root
fi

exec npm-install.sh bower-install.sh pip-install.sh setup-postgres.sh "${@:-bash}"
