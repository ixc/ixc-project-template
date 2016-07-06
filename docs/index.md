# Overview

TODO

# Table of Contents

  * [Changelog][changelog]
  * [Contributing][contributing]

# Quick Start

First, follow our [Docker Quick Start][docker-quick-start] guide to get Docker
installed and familiarise yourself with some of its basic commands.

Clone the repository:

    $ git clone git@github.com:ixc/{{ project_name }}.git

Run the project with [Docker][docker]:

    $ cd {{ project_name }}
    $ docker-compose up

Local NPM packages, Bower components and python packages will be installed on
first run, which might take a few minutes, so make yourself a cup of tea.
Subsequent runs will only update local packages when dependencies have changed.

That's it! Open the site in a browser:

    http://{{ project_name }}.lvh.me:8000  # Docker for Mac/Win, Linux
    http://{{ project_name }}.docker:8000  # OS X with Dinghy

## Container Entrypoint

The entrypoint scripts take care of a few things for us:

  * Install NPM packages, Bower components, and Python packages, to ensure the
    local environment matches the local dependencies.

  * Wait up to 10 seconds for PostgreSQL to become available, so Django doesn't
    complain about being unable to connect.

  * Derive the database name from the current git branch, so we can switch
    branches without losing our working database.

  * Create a database, and optionally restore from a file or source database.

  * Apply Django migrations, if required.

  * Run `manage.py supervisor`.

  * Use [Gulp][gulp] to watch the file system to automatically update NPM
    packages, Bower components and Python packages when dependencies change,
    and restart supervisor when Python source changes.

## Shared Directories

The `docker-compose.yml` file bind mounts a few directories directly into the
container:

  * `.` at `/opt/{{ project_name }}` - Your local changes will be visible
    immediately, and you won't need to rebuild the image to test every change.

  * `~/.ssh` at `/root/.ssh`, so you can access private git repositories inside
    the container.

## Local Settings

Your `local.py` will be available in the container as part of the bind mounted
project directory, but it won't be included in the built image.

You should add secrets to `docker-compose.override.yml` and use `local.py` only
for true local overrides, like which DDT panels are enabled.

# Manual Installation

Clone the repository and change directory:

    $ git clone git@github.com:ixc/{{ project_name }}.git
    $ cd {{ project_name }}

Manually install system dependencies (check `Dockerfile` for hints).

Install Node modules:

    $ npm install

Install Bower components:

    $ ./node_modules/.bin/bower install

Create a virtualenv and install Python packages:

    $ pip install -U virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt -e . -i https://ic:{password}@devpi.ixcsandbox.com/ic/dev/+simple/

If you want to install in-development dependencies as editable VCS installs:

    (venv)$ pip install -r requirements-dev.txt

Add secrets to `local.py`:

    (venv)$ cp djangosite/settings/local.sample.py djangosite/settings/local.py
    (venv)$ $EDITOR djangosite/settings/local.py

Create a database and apply migrations:

    (venv)$ createdb {{ project_name }}
    (venv)$ ./manage.py migrate

# Supervisor

Use [django-supervisor][django-supervisor] to run the project (e.g. `wsgi` and
other processes):

    (venv)$ ./manage.py supervisor

You can also execute other [supervisor][supervisor] actions:

    (venv)$ ./manage.py supervisor restart all
    (venv)$ ./manage.py supervisor shell
    (venv)$ ./manage.py supervisor status

# HTML Docs

Docs are written in [Markdown][markdown]. You can use [MkDocs][mkdocs] to preview your
documentation as you are writing it:

    (venv)$ mkdocs serve

It will even auto-reload whenever you save any changes, so all you need to do
to see your latest edits is refresh your browser.

[changelog]: changelog.md
[contributing]: contributing.md
[django-supervisor]: https://github.com/rfk/django-supervisor
[docker]: https://www.docker.com/
[docker-quick-start]: https://github.com/ixc/django-icekit/blob/feature/demo/docs/docker-quick-start.md
[gulp]: https://github.com/gulpjs/gulp
[markdown]: http://daringfireball.net/projects/markdown/
[mkdocs]: http://mkdocs.org
[supervisor]: http://supervisord.org/
