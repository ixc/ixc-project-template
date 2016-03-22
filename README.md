# Readme

Docs can be found in the [docs](docs/index.md) folder.

## Project Template

This is a bare-bones skeleton project template, for use with the
`django-admin.py startproject` command.

You will need `git`, `python 2.7+` and `pip` to create a new project with this
template.

Create a new project from the template with:

    $ curl -L http://bit.ly/ixc-project-template | bash -s <project-name> [template path or URL]

This will:

  * Install Django, if necessary.

  * Create a directory matching the given project name in the current working
    directory.

  * Replaces non-word characters in the project name with an underscore, to get
    a valid Python module name for the project.

  * Call `django-admin.py startproject`, with the derived module name and given
    template path or URL. If none is given, it defaults to
    https://github.com/ixc/ixc-project-template/archive/master.zip

  * Make `manage.py` executable, for convenience.

  * Initialize a git repository and add all files in an initial commit.

  * Add an `origin` remote at `git@github.com:ixc/{project-name}.git`

Then you will need to follow a few some manual steps that are printed by the
`startproject.sh` script.
