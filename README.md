# ICEkit Project Template

This is a project template for the ICEkit CMS.

You will need `bash`, `curl`, and Python 2.7+ to create a new project with this
template, and Docker to follow the quick start instructions.

## Quick Start

First, follow our [Docker Quick Start][docker-quick-start] guide to get Docker
installed and familiarise yourself with some of its basic commands.

Create a new project from this template with:

    $ bash <(curl -L https://raw.githubusercontent.com/ixc/ixc-project-template/master/startproject.sh) <project_name> [destination_dir]

Run the project:

    $ cd <project_name>
    $ docker-compose up

Some local setup will be performed on first run, which might take a while, so
make yourself a cup of tea. Subsequent runs will skip the local setup unless
the project dependencies have been updated.

That's it! Open the site in a browser:

    http://<project_name>.docker:8000  # OS X with Dinghy
    http://<project_name>.lvh.me:8000  # Linux or Docker for Mac/Win

[docker-quick-start]: https://github.com/ixc/django-icekit/blob/feature/demo/docs/docker-quick-start.md
