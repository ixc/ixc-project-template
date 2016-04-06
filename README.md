# Project Template

This is a project template for the ICEkit CMS.

You will need `git`, `python 2.7+` and `pip` to create a new project with this
template.

Create a new project from the template with:

    $ curl -L http://bit.ly/django-icekit-template | bash -s {project_name} [template path or URL]

This will:

  * Install Django, if necessary.

  * Create a directory matching the given project name in the current working
    directory.

  * Replace non-word characters in the project name with an underscore, to get
    a valid Python package name for the project.

  * Call `django-admin.py startproject`, with the derived package name and
    given template path or URL. The default template URL is
    https://github.com/ixc/ixc-project-template/archive/django-icekit.zip

  * Make `manage.py` executable, for convenience.

  * Initialize a git repository and add all files in an initial commit.

Then you will need to follow a few some manual steps that are printed by the
`startproject.sh` script.

# Readme

Docs can be found in the [docs](docs/index.md) folder.

# Quick Start

Install Docker. For more detail, check our [Docker docs].

Clone the repository:

    $ git clone git@github.com:ixc/{{ project_name }}.git

Run the project:

    $ cd {{ project_name }}
    $ docker-compose up

Open the site in a browser:

    $ open http://{{ project_name }}.docker:8000  # OS X
    $ open http://{{ project_name }}.lvh.me:8000  # Linux

[Docker docs]: docker.md
