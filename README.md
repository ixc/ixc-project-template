# Readme

Docs can be found in the [docs](docs/index.md) folder.

## Project Template

This is a bare-bones skeleton project template, for use with the
`django-admin.py startproject` command.

You will need `bower`, `django 1.4+`, `git`, `npm`, `python 2.7+`, `pip` and
`virtualenv`  to create a new project with this template.

    # Create environment variable for the project name, so we can use it in the
    # following commands.
    $ export PROJECT=<project_name>

    # Create project from template.
    $ mkdir -p ~/Projects
    $ django-admin.py startproject -e json,md -n .gitignore,base.html \
    --template=https://github.com/ixc/ixc-project-template/archive/master.zip \
    $PROJECT

    # Make `manage.py` executable, for convenience.
    $ cd $PROJECT
    $ chmod 755 manage.py

    # Create git repository and push initial commit.
    $ git init
    $ git add -A
    $ git commit -m 'Initial commit.'
    $ git remote add origin git@github.com:ixc/$PROJECT.git
    $ git push

    # Create virtualenv and install Python requirements.
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt

    # Install optional and environment-specific Python requirements.
    (venv)$ pip install ipdb ipython mkdocs psycopg2

    # Install front-end requirements.
    (venv)$ bower install

    # Configure the local settings module.
    (venv)$ cp djangosite/settings/local.tmpl.py djangosite/settings/local.py
    (venv)$ vi djangosite/settings/local.py

    # Sync the database.
    (venv)$ ./manage.py syncdb --noinput
    (venv)$ ./manage.py migrate

Now start work on your project! You might want to start with:

  * Remove the `Project Template` section (these instructions) from
    `README.md` (this file).
  * Update `djangosite/settings/*.py` (e.g. enable apps, middleware, etc.)
  * Update `requirements.txt` (e.g. add dependencies for installed apps, etc.)
