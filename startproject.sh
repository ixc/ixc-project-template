#!/bin/bash

set -e

# Use "-" as separator for project (directory) name. Use "_" as separator for
# module name.
PROJECT_NAME="${1//[^0-9A-Za-z]/-}"
PACKAGE_NAME="${1//[^0-9A-Za-z]/_}"

# Use project name as default destination directory.
DEST_DIR="${2-:${PROJECT_NAME}}"

# Hard code template URL.
TEMPLATE="https://github.com/ixc/ixc-project-template/archive/django-icekit.zip"

# Abort if Python is not available.
if [[ -z $(which python) ]]; then
	echo 'Python is not available. Aborting.'
	exit 1
fi

# Abort if the destination directory already exists.
if [[ -d "${DEST_DIR}" ]]; then
	echo "Project directory '${DEST_DIR}' already exists. Aborting."
	exit 1
fi

cat <<EOF

This script will create a new ICEkit project in directory '${DEST_DIR}' and
with Python package name '${PACKAGE_NAME}'."

It might need to install 'pip' and 'virtualenv' into your global environment,
and will prompt for confirmation if it does.

EOF

read -p 'Press CTRL-C to abort or any other key to continue...'
echo

# Install Pip, if we need to.
if [[ -z $(which pip) ]]; then
	echo 'Pip is not available. Installing.'
	read -p 'Press CTRL-C to abort or any other key to continue...'
	echo

	if [[ -n $(which curl) ]]; then
		curl -L https://bootstrap.pypa.io/get-pip.py | python
	elif [[ -n $(which wget) ]]; then
		wget https://bootstrap.pypa.io/get-pip.py | python
	else
		cat <<EOF

Neither 'curl' or 'wget' is available. Please install one or the other and try
again. Aborting.

EOF
		exit 1
	fi
fi

# Install virtualenv, if we need to.
if [[ -z $(which virtualenv) ]]; then
	echo
	echo 'Virtualenv is not available. Installing.'
	echo
	read -p 'Press CTRL-C to abort or any other key to continue...'
	echo
	pip install virtualenv
fi

# Install Django into a temporary virtualenv.
echo 'Installing Django into temporary virtualenv.'
virtualenv "/tmp/${PROJECT_NAME}-venv"
source "/tmp/${PROJECT_NAME}-venv/bin/activate"
pip install Django

# Create project directory, to silence `django-admin.py startproject` error
# when specifying a destination directory.
if [[ ! -d "${DEST_DIR}" ]]; then
	echo "Creating project directory '${DEST_DIR}'."
	mkdir -p "${DEST_DIR}"
fi

# Create project from template.
echo "Creating project from template '${TEMPLATE}'."
django-admin.py startproject \
	-e json,ini,md,yml \
	-n .coveragerc,base.html,Dockerfile \
	--template="${TEMPLATE}" \
	"${PACKAGE_NAME}" \
	"${DEST_DIR}"

# Remove temporary virtualenv, if it exists.
if [[ -d "/tmp/${PROJECT_NAME}-venv" ]]; then
	echo 'Removing temporary virtualenv.'
	deactivate
	rm -rf "/tmp/${PROJECT_NAME}-venv"
fi

cd "${DEST_DIR}"

echo "Removing vestigial 'startproject.sh' script."
rm -f startproject.sh

echo "Making 'bin/*.sh' and 'manage.py' scripts executable."
chmod 755 bin/*.sh manage.py

if [[ -n $(which git) ]]; then
	echo
	read -p 'Would you like to initialize a Git repository for your new project and create an initial commit? (Y/n) ' -n 1 -r
	echo
	if [[ "${REPLY:-y}" =~ ^[Yy]$ ]]; then
		git init
		git add -A
		git commit -m 'Initial commit.'
	fi
fi

cat <<EOF

All done!

If you have Docker installed, you can run your new ICEkit project immediately
with:

	$ cd ${DEST_DIR}
	$ docker-compose up

Otherwise, check out our [Docker Quick Start][0] guide or [Manual Setup][1]
guide to finish setting up your new ICEkit project.

[0]: https://github.com/ixc/django-icekit/docs/docker-quick-start.md
[1]: https://github.com/ixc/django-icekit/docs/manual-setup-guide.md

EOF
