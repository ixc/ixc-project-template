# Readme

Docs can be found in the [docs](docs/index.md) folder.

## Project Template

This is a bare-bones skeleton project template, for use with the
`django-admin.py startproject` command.

You will need `git`, `python 2.7+` and `pip` to create a new project with this
template.

Create environment variables for the project and module name (e.g. `foo-bar`
and `foo_bar`), so we can use them in subsequent commands:

    $ export PROJECT=<project_name>
    $ export MODULE=<module_name>

Install or upgrade Django:

    $ pip install -U Django

Create a project from the template:

    $ mkdir $PROJECT
    $ django-admin.py startproject -e json,ini,md,yml -n base.html,.coveragerc \
    --template=https://github.com/ixc/ixc-project-template/archive/master.zip \
    $MODULE $PROJECT

Make the `manage.py` file executable, for convenience:

    $ cd $PROJECT
    $ chmod 755 manage.py

Create a remote repository on [GitHub](https://github.com), then initialise a
local repository and push an initial commit:

    $ git init
    $ git add -A
    $ git commit -m 'Initial commit.'
    $ git remote add origin git@github.com:ixc/$PROJECT.git
    $ git push

Now, get to work on your project! You might want to start with:

  * Add a `LICENSE.txt` file (e.g.
    [MIT](http://choosealicense.com/licenses/mit/)).
  * Read the [contributing](docs/contributing.md) docs.
  * Update the [docs](docs/index.md) (e.g. overview, installation and usage).
  * Remove the `Project Template` section (these instructions) from `README.md`
    (this file).
