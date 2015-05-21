# Readme

Docs can be found in the [docs](docs/index.md) folder.

## Project Template

This is a bare-bones skeleton project template, for use with the
`django-admin.py startproject` command.

You will need `django 1.4+`, `git`, `python 2.7+`, `pip`, and `virtualenv` to
create a new project with this template.

Create environment variables for the project and module name (e.g. `foo-bar`
and `foo_bar`), so we can use them in subsequent commands:

    $ export PROJECT=<project_name>
    $ export MODULE=<module_name>

Create a project from the template:

    $ mkdir $PROJECT
    $ django-admin.py startproject -e json,md,yml -n base.html \
    --template=https://github.com/ixc/ixc-project-template/archive/master.zip \
    $MODULE $PROJECT

Make the `manage.py` file executable, for convenience:

    $ cd $PROJECT
    $ chmod 755 manage.py

Create a remote repository on [GitHub], then initialise a local repository and
push an initial commit:

    $ git init
    $ git add -A
    $ git commit -m 'Initial commit.'
    $ git remote add origin git@github.com:ixc/$PROJECT.git
    $ git push

Create a virtualenv and install the dependencies:

    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt -e .[dev,postgres,test]  # Omit unwanted optional extras.

Run the tests:

    (venv)$ tox

Now, write your project! You might want to start with:

  * Remove the `Project Template` section (these instructions) from `README.md`
    (this file).
  * Add a `LICENSE` file (e.g. [MIT]).
  * Update the `docs/index.md` file (e.g. the overview, installation and usage
    sections).
  * Read the [contributing] docs.

[contributing]: docs/contributing.md
[GitHub]: https://github.com
[MIT]: http://choosealicense.com/licenses/mit/
