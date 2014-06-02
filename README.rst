How to use
==========

This is a bare-bones skeleton project template, for use with the
``django-admin.py startproject`` command.

It is assumed that your development environment is already setup, including
having globally installed Django 1.4+ and ``virtualenvwrapper``.

Create a new project like this:

1.  Define a ``$PROJECT`` variable, so we can copy and paste the following
    commands::

        $ export PROJECT=<PROJECT_NAME>

    ``<PROJECT_NAME>`` should be a valid Python module name.

2.  Change to your ``projects`` directory and create a new project from this
    template::

        $ cd ~/projects
        $ django-admin.py startproject -n base.html -n deployo.json -n index.rst \
        -n Makefile -n make.bat -n project_base.html -n README.rst \
        --template=https://github.com/ixc/ixc-project-template/archive/master.zip \
        $PROJECT

3.  Change to the project directory and make ``manage.py`` executable::

        $ cd $PROJECT
        $ chmod 755 manage.py

4.  Create a ``virtualenv`` for the project and pin its dependencies::

        $ mkvirtualenv -a "$PWD" -r requirements-unpinned.txt $PROJECT
        $ pip freeze > requirements.txt

5.  Create a private repository with the same name as your project owned by the
    IxC account at `GitHub <https://github.com/ixc/>`_.

6.  Initialize the project directory as a Git repository and push an initial
    commit::

        $ git init
        $ git add -A
        $ git commit -m 'Initial commit.'
        $ git remote add origin git@github.com:ixc/$PROJECT.git
        $ git push

You're almost ready to start developing. First, complete your local deployment:

7.  Create and update a local deployment settings module from the template::

        $ cp djangosite/settings/local.tmpl.py djangosite/settings/local.py
        $ vi djangosite/settings/local.py

The rest is up to you. Here are a few things you might want to start with:

*   Update the ``README.rst`` file (this file). Remove the ``How to use``
    section (these instructions) and update the rest to suit your project.

*   Update the ``settings/*.py`` files with project level settings.

*   Update the ``requirements.txt`` file with additional dependencies. There
    are many optional dependencies in the ``requirements-unpinned.txt`` file
    (commented out), as well as instructions on how to pull a dependency into
    this project with ``git subtree``.


Overview
========

Description of your project.


Installation
============

You will need Git, Python 2.6.5+ or 3.2+, ``pip``, ``virtualenv`` and
``virtualenvwrapper`` to install this project and its dependencies. Find more
info on how to setup a development environment on our internal wiki.

1.  Clone the project from GitHub to your ``projects`` folder::

        $ cd ~/projects
        $ git clone git@github.com:ixc/{{ project_name }}.git

2.  Change to the project directory, create a ``virtualenv`` and install its
    dependencies::

        $ cd {{ project_name }}
        $ mkvirtualenv -a "$PWD" {{ project_name }}
        $ pip install -r requirements.txt

3.  Configure the project settings for the local environment::

        ({{ project_name }})$ cp djangosite/settings/local.tmpl.py djangosite/settings/local.py
        ({{ project_name }})$ vi djangosite/settings/local.py

4.  Sync the database, load ORM fixtures and download bower components::

        ({{ project_name }})$ ./manage.py syncdb --migrate --noinput
        ({{ project_name }})$ ./manage.py orm_fixtures
        ({{ project_name }})$ ./manage.py bower_install

5.  If deploying to a development environment, you can also load the
    ``sample_data`` ORM fixture::

        ({{ project_name }})$ ./manage.py orm_fixtures sample_data

    This will create a ``admin@example.com`` superuser with the password
    ``admin123``.

6.  If deploying to a production environment, collect static files for
    installed apps::

        ({{ project_name }})$ ./manage.py collectstatic


Working with the project
========================

Activate the ``virtualenv`` and change to project directory::

    $ workon {{ project_name }}

Run management commands::

    ({{ project_name }})$ ./manage.py runserver
    ({{ project_name }})$ ./manage.py shell
    ...

When you are done, deactivate the ``virtualenv``::

    ({{ project_name }})$ deactivate

