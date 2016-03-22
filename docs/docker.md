# Docker

You can run this project with Docker to ensure identical local development and
production environments.

## Docker Setup (OS X)

Install [Homebrew]:

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install [Docker Toolbox]:

    $ brew tap caskroom/cask
    $ brew cask install dockertoolbox

Install [Dinghy]:

    $ brew tap codekitchen/dinghy
    $ brew install dinghy

Create a new host VM:

    $ dinghy create --provider vmware  # Omit `provider` for Virtualbox

Configure Docker to use the host VM:

    $ eval "$(dinghy shellinit)"
    $ echo 'eval "$(dinghy shellinit)"' >> ~/.profile

## Why Dinghy?

Dinghy makes Docker a little nicer to work with on OS X, which cannot run
Docker natively and must run inside a VM. Here's how:

  * Faster volume sharing using NFS rather than built-in virtualbox/vmware
    file shares.
  * Filesystem events work on mounted volumes.
  * Easy access to running containers using built-in DNS and HTTP proxy.

## Project Setup

Clone the project:

    $ git clone git@github.com:ixc/{{ project_name }}.git

Create a `docker-compose.override.yml` for secrets and local settings:

    $ cd {{ project_name }}
    $ cp docker-compose.override.sample.yml docker-compose.override.yml
    $ $EDITOR docker-compose.override.yml

Use [Docker Compose] to build all the services defined in the compose file:

    $ docker-compose build

## Local Development

Run all services:

    $ docker-compose up

Open the site in a browser:

    $ open http://{{ project_name }}.docker:8000

Run a command in a new `django` service container, and remove the container
afterwards:

    $ docker-compose run --rm django python manage.py migrate

Run a command in an already running container:

    $ docker exec -it {{ project_name }}_django_1 bash

## Entrypoint

The default entrypoint scripts take care of a few things for us:

  * Create and switch to an unprivileged user.
  * Ensure the unprivileged user and variable files directory have the same UID
    and GID.
  * Derive the database name from the current git branch, when bind mounting
    the source into the container.
  * Wait up to 10 seconds for PostgreSQL to become available.
  * Create the database, and optionally restore from a file or source database.
  * Apply Django migrations, if they have changed.

In particular, the automated database creation, restore, and migrations make it
much easier to switch between and test feature branches in isolation, without
losing your current data.

## Gulp

The `docker-compose.sample.yml` file uses [Gulp] as the default command, which
watches the file system and automates a few tasks when changes are detected:

  * Restart the main command when `*.py` files are changed.
  * Reinstall Node.js packages when `package.json` is changed.
  * Reinstall Bower components when `bower.json` is changed.
  * Reinstall Python packages when `setup.py` is changed.

## Shared Directories

The `docker-compose.override.sample.yml` file bind mounts a few directories
directly into the container:

  * `.` at `/opt/{{ project_name }}` - Your local changes will be visible
    immediately, and you won't need to rebuild the image to test every change.

  * `./var` at `/opt/{{ project_name }}/var` - For variable data like logs,
    media, etc. This is normally a data volume, so we need to bind mount it
    even though `.` is already mounted.

## Local Settings

Your `local.py` will be available in the container as part of the bind mounted
project directory, but it won't be included in the built image.

You should add secrets to `docker-compose.override.yml` and use `local.py` only
for true local overrides, like which DDT panels are enabled.

[Dinghy]: https://github.com/codekitchen/dinghy
[Docker Compose]: https://docs.docker.com/compose/
[Docker Toolbox]: https://www.docker.com/toolbox
[Gulp]: https://github.com/gulpjs/gulp
[Homebrew]: http://brew.sh/
