# Overview

TODO

## Table of Contents

  * [Changelog]
  * [Contributing]

## Installation

You will need `git`, `python 2.7+` and `pip` to install this project and its
dependencies.

Clone the repository and change directory:

    $ git clone git@github.com:ixc/<project_name>.git
    $ cd <project_name>

Install binary and frontend dependencies:

    $ brew tap homebrew/bundle
    $ brew bundle
    $ npm install -g bower
    $ bower install

If you are not using OS X with [Homebrew], you will need to install
the packages listed in the `Brewfile` file manually.

Create a virtualenv and install dependencies:

    $ pip install -U virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt  # Absolute dependencies.
    (venv)$ pip install -e .[dev,postgres,test]  # Abstract dependencies. Remove `dev`, `postgres` or `test` if unwanted.

You MUST **review and uncomment** the appropriate environment specific
configuration in the local settings module:

    (venv)$ cp djangosite/settings/local.tmpl.py djangosite/settings/local.py
    (venv)$ $EDITOR djangosite/settings/local.py

Migrate the database and collect static files:

    (venv)$ ./manage.py migrate
    (venv)$ ./manage.py collectstatic  # If `DEBUG=False`.

## Usage

Use [django-supervisor] to run the project (e.g. gunicorn and other processes):

    (venv)$ ./manage.py supervisor

You can also execute other [supervisor] actions:

    (venv)$ ./manage.py supervisor restart all
    (venv)$ ./manage.py supervisor shell
    (venv)$ ./manage.py supervisor status

## HTML Docs

Docs are written in [Markdown]. You can use [MkDocs] to preview your
documentation as you are writing it:

    (venv)$ mkdocs serve

It will even auto-reload whenever you save any changes, so all you need to do
to see your latest edits is refresh your browser.

[Changelog]: changelog.md
[Contributing]: contributing.md
[django-supervisor]: https://github.com/rfk/django-supervisor
[Homebrew]: http://brew.sh/
[Markdown]: http://daringfireball.net/projects/markdown/
[MkDocs]: http://mkdocs.org
[supervisor]: http://supervisord.org/
