# Overview

*Write a description of your project.*

## Table of Contents

  * [Changelog]
  * [Contributing]

## Installation

You will need `bower`, `git`, `npm`, `python 2.7+`, `pip`, and `virtualenv` to
install this project and its dependencies.

    # Clone the project.
    $ mkdir -p ~/Projects
    $ cd ~/Projects
    $ git clone git@github.com:ixc/{{ project_name }}.git

    # Create virtualenv and install Python requirements.
    $ cd {{ project_name }}
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

    # Run optional and environment-specific management commands
    (venv)$ ./manage.py orm_fixtures sample_data
    (venv)$ ./manage.py collectstatic

## Usage

This project uses [django-supervisor] to start all its required processes (e.g.
web server, celery):

    (venv)$ ./manage.py supervisor

This provides a few benefits:

  * A single point of control for running the project, `manage.py`.
  * Running the project is as easy in development as in production.
  * All processes get auto-reloading when `DEBUG=True`.
  * Process configuration can access Django's settings module.

You can also execute other [supervisor] actions:

    (venv)$ ./manage.py supervisor restart
    (venv)$ ./manage.py supervisor shell
    (venv)$ ./manage.py supervisor status

## HTML docs

Docs are written in [Markdown]. You can use [MkDocs] to build a static HTML
version that you can host anywhere:

    (venv)$ mkdocs build

Or you can use the built-in dev server to preview your documentation as you're
writing it:

    (venv)$ mkdocs serve

It will even auto-reload whenever you save any changes, so all you need to do
to see your latest edits is refresh your browser.

[Changelog]: changelog.md
[Contributing]: contributing.md
[django-supervisor]: https://github.com/rfk/django-supervisor
[Markdown]: http://daringfireball.net/projects/markdown/
[MkDocs]: http://mkdocs.org
[supervisor]: http://supervisord.org/
