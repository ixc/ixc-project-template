# ICEkit Project Template

This is a project template for the ICEkit CMS.

You will need `git`, `python 2.7+` and `pip` to create a new project with this
template. To follow the Quick start instructions, you will also need [Docker] (see [Docker instructions]).

## Quick start

Download this template and create a new project with:

    $ curl -L http://bit.ly/django-icekit-template | bash -s {project_name} [template path or URL]

Install dependencies and run the project:

    $ cd {{ project_name }}
    $ docker-compose up

Make a cup of tea, as Docker will take a while to download and install the dependencies.
You can run `docker-compose up` each time you work on the project - it will check for
changed dependencies and only install those.

That's it! Open the site in a browser:

    $ open http://{{ project_name }}.docker:8000  # OS X
    $ open http://{{ project_name }}.lvh.me:8000  # Linux

## Documenation

Docs can be found in the [docs](docs/index.md) folder.

[Docker]: https://www.docker.com
[Docker instructions]: docker.md
