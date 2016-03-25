# Overview

TODO

# Table of Contents

  * [Changelog]
  * [Contributing]

# Quick Start

First, install Docker. For more detail, check our [Docker docs].

Clone the repository:

    $ git clone git@github.com:ixc/{{ project_name }}.git

Run the project:

    $ cd {{ project_name }}
    $ docker-compose up

Open the site in a browser:

    $ open http://{{ project_name }}.docker:8000  # OS X
    $ open http://{{ project_name }}.lvh.me:8000  # Linux

# Manual Installation

You will need `git`, `python 2.7+` and `pip` to install this project and its
dependencies.

Clone the repository and change directory:

    $ git clone git@github.com:ixc/{{ project_name }}.git
    $ cd {{ project_name }}

Install system and frontend dependencies:

    $ brew bundle  # OS X only. Otherwise, manually install packages listed in `Brewfile`.
    $ npm install -g bower
    $ bower install

Create a virtualenv and install dependencies:

    $ pip install -U virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -e '.[dev]' -i https://ic:{password}@devpi.ixcsandbox.com/ic/dev/+simple/

If you want to install in-development dependencies as editable VCS installs:

    (venv)$ pip install -r requirements-dev.txt

Review and update the appropriate environment specific configuration in the
local settings module:

    (venv)$ cp djangosite/settings/local.sample.py djangosite/settings/local.py
    (venv)$ $EDITOR djangosite/settings/local.py

Migrate the database:

    (venv)$ ./manage.py migrate

# Usage

Use [django-supervisor] to run the project (e.g. `wsgi` and other processes):

    (venv)$ ./manage.py supervisor

You can also execute other [supervisor] actions:

    (venv)$ ./manage.py supervisor restart all
    (venv)$ ./manage.py supervisor shell
    (venv)$ ./manage.py supervisor status

# HTML Docs

Docs are written in [Markdown]. You can use [MkDocs] to preview your
documentation as you are writing it:

    (venv)$ mkdocs serve

It will even auto-reload whenever you save any changes, so all you need to do
to see your latest edits is refresh your browser.

[Changelog]: changelog.md
[Contributing]: contributing.md
[django-supervisor]: https://github.com/rfk/django-supervisor
[Docker docs]: docker.md
[Homebrew]: http://brew.sh/
[Markdown]: http://daringfireball.net/projects/markdown/
[MkDocs]: http://mkdocs.org
[supervisor]: http://supervisord.org/
