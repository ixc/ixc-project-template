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
git remote add origin "git@github.com:ixc/${PROJECT}.git"

cat <<EOF

All done!

Now, you need to manually create the 'ixc/${PROJECT}' repository on GitHub and
push your initial commit.

Then, you can get to work on your project! You might want to start with:

  * Add a 'LICENSE.txt' file - [MIT](http://choosealicense.com/licenses/mit/)
  * Read the [contributing](docs/contributing.md) docs.
  * Update the [docs](docs/index.md) (e.g. overview, installation and usage).
  * Remove the 'Project Template' section (these instructions) from
    'README.md'.

EOF
