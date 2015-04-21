# Overview

TODO

## Table of Contents

  * [Changelog]
  * [Contributing]

## Installation

You will need `bower`, `git`, `python 2.7+`, `pip`, and `virtualenv` to install
this project and its dependencies.

Clone the project:

    $ git clone git@github.com:ixc/<project_name>.git

Create a virtualenv and install the dependencies:

    $ cd <project_name>
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt
    (venv)$ pip install psycopg2  # if using PostgreSQL
    (venv)$ bower install

You MUST **review and uncomment** the appropriate environment specific
configuration in the local settings module:

    (venv)$ cp djangosite/settings/local.tmpl.py djangosite/settings/local.py
    (venv)$ $EDITOR djangosite/settings/local.py

## Usage

Migrate the database and collect static files:

    (venv)$ ./manage.py migrate
    (venv)$ ./manage.py collectstatic  # if `DEBUG=False`

Use [django-supervisor] to run the project (e.g. gunicorn and other processes):

    (venv)$ ./manage.py supervisor

You can also execute other [supervisor] actions:

    (venv)$ ./manage.py supervisor restart
    (venv)$ ./manage.py supervisor shell
    (venv)$ ./manage.py supervisor status

## HTML Docs

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
