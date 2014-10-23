How to use
==========

This is a bare-bones skeleton project template, for use with the
`django-admin.py startproject` command.

You will need `Git`, `Python 2.7+` or `Python 3.2+`,
`pip`, `virtualenv`, `virtualenvwrapper`, `bower` and `npm` to
create a new project with this template.

Create a new project like this:

 1. Define a `$PROJECT` variable, so we can copy and paste the following
    commands:

        $ export PROJECT=<PROJECT_NAME>

    `<PROJECT_NAME>` should be a valid Python module name.

 2. Change to your `projects` directory and create a new project from this
    template:

        $ cd ~/projects
        $ django-admin.py startproject -n .gitignore -n base.html -n \
        bower.json -n deployo.json -n index.rst -n Makefile -n make.bat -n \
        README.md --template=https://github.com/ixc/ixc-project-template/archive/master.zip \
        $PROJECT

 3. Change to the project directory and make `manage.py` executable:

        $ cd $PROJECT
        $ chmod 755 manage.py

 4. Create a `virtualenv` for the project and pin its dependencies:

        $ mkvirtualenv -a "$PWD" $PROJECT
        $ pip install -r requirements-unpinned.txt
        $ pip freeze > requirements.txt

 5. Create a private repository with the same name as your project owned by the
    [IxC account at GitHub](https://github.com/ixc/).

 6. Initialize the project directory as a Git repository and push an initial
    commit:

        $ git init
        $ git add -A
        $ git commit -m 'Initial commit.'
        $ git remote add origin git@github.com:ixc/$PROJECT.git
        $ git push

You're almost ready to start developing. First, complete your local deployment:

 7. Create and update a local deployment settings module from the template:

        $ cp djangosite/settings/local.tmpl.py djangosite/settings/local.py
        $ vi djangosite/settings/local.py

The rest is up to you. Here are a few things you might want to start with:

  * Update the `README.md` file (this file). Remove the `How to use`
    section (these instructions) and update the rest to suit your project.

  * Update the `djangosite/settings/*.py` files to enable apps that will be
    used by this project.

  * Update the `requirements-unpinned.txt` file with additional dependencies.

  * Use `pip freeze > requirements.txt` to pin the versions for all of your
    dependencies.


Overview
========

Description of your project.


Installation
============

You will need `Django 1.4+`, `Git`, `Python 2.7+` or `Python 3.2+`,
`pip`, `virtualenv`, `virtualenvwrapper`, `bower` and `npm` to
install this project and its dependencies.

 1. Clone the project from GitHub to your `projects` folder:

        $ cd ~/projects
        $ git clone git@github.com:ixc/{{ project_name }}.git

 2. Change to the project directory, create a `virtualenv` and install its
    core dependencies:

        $ cd {{ project_name }}
        $ mkvirtualenv -a "$PWD" {{ project_name }}
        ({{ project_name }})$ pip install -r requirements.txt

 3. You might also want to install some of the following development and
    production deployment specific dependencies:

        ({{ project_name }})$ pip install ipdb
        ({{ project_name }})$ pip install psycopg2

 4. Download bower components:

        ({{ project_name }})$ bower install

 5. Configure the project settings for the local environment:

        ({{ project_name }})$ cp djangosite/settings/local.tmpl.py \
        djangosite/settings/local.py
        ({{ project_name }})$ vi djangosite/settings/local.py

 6. Sync the database, load ORM fixtures:

        ({{ project_name }})$ ./manage.py syncdb --migrate --noinput
        ({{ project_name }})$ ./manage.py orm_fixtures

 7. If deploying to a development environment, you can also load the
    `sample_data` ORM fixture:

        ({{ project_name }})$ ./manage.py orm_fixtures sample_data

    This will create a `admin@example.com` superuser with the password
    `admin123`.

 8. If deploying to a production environment, collect static files for
    installed apps:

        ({{ project_name }})$ ./manage.py collectstatic


Working with the project
========================

Activate the `virtualenv` and change to project directory:

    $ workon {{ project_name }}

Run management commands:

    ({{ project_name }})$ ./manage.py supervisor
    ({{ project_name }})$ ./manage.py shell
    ...

When you are done, deactivate the `virtualenv`:

    ({{ project_name }})$ deactivate

