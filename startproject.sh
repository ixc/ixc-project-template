#!/bin/bash

set -e

PROJECT="$1"
MODULE="${PROJECT//[^0-9A-Za-z]/_}"
TEMPLATE="${2:-https://github.com/ixc/ixc-project-template/archive/master.zip}"

if [[ -d "${PROJECT}" ]]; then
	echo "Project directory '${PWD}/${PROJECT}' already exists. Abort."
	exit 1
fi

if [[ -z $(which django-admin.py) ]]; then
	echo 'Django is missing. Install.'
	pip install Django
fi

echo "Creating project directory '${PWD}/${PROJECT}'"
mkdir "${PWD}/${PROJECT}"

echo "Creating project from template '${TEMPLATE}'"
django-admin.py startproject \
	-e json,ini,md,yml \
	-n .coveragerc,base.html,Dockerfile \
	--template="${TEMPLATE}" \
	"${MODULE}" "${PROJECT}"

cd "${PROJECT}"

echo "Making '${PWD}/manage.py' executable."
chmod 755 manage.py

echo "Initializing git repository and creating an initial commit."
git init
git add -A
git commit -m 'Initial commit.'

cat <<EOF

All done!

Well, except for a few manual steps:

  * Add an `origin` remote at `git@github.com:{YOU}/${PROJECT}.git`
  * Create the '{YOU}/${PROJECT}' repository on GitHub.
  * Enable the repository on Travis CI and add the 'DOCKER_PASSWORD' and
    'PIP_INDEX_URL' environment variables in the repository settings.
  * Push your initial commit.

Then, you can get to work on your project! You might want to start with:

  * Add a 'LICENSE.txt' file - [MIT](http://choosealicense.com/licenses/mit/)
  * Read the [contributing](docs/contributing.md) docs.
  * Update the [docs](docs/index.md) (e.g. overview, installation and usage).
  * Remove the 'Project Template' section (these instructions) from
    'README.md'.

EOF
