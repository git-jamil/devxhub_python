=====
Usage
=====

Grab a django-boilerplate template
----------------------------

First, clone a django-boilerplate project template::

    $ git clone https://github.com/git-jamil/django-boilerplate.git

Make your changes
-----------------

Modify the variables defined in `devxhub_python.json`.

Open up the skeleton project. If you need to change it around a bit, do so.

You probably also want to create a repo, name it differently, and push it as
your own new django-boilerplate project template, for handy future use.

Generate your project
---------------------

Then generate your project from the project template::

    $ devxhub_python django-boilerplate/

The only argument is the input directory. (The output directory is generated
by rendering that, and it can't be the same as the input directory.)

.. note:: see :ref:`command_line_options` for extra command line arguments

Try it out!



Works directly with git and hg (mercurial) repos too
------------------------------------------------------

To create a project from the django-boilerplate.git repo template::

    $ devxhub_python gh:devxhub/django-boilerplate

devxhub_python knows abbreviations for Github (``gh``), Bitbucket (``bb``), and
GitLab (``gl``) projects, but you can also give it the full URL to any
repository::

    $ devxhub_python https://github.com/git-jamil/django-boilerplate.git
    $ devxhub_python git@github.com:git-jamil/django-boilerplate.git

You will be prompted to enter a bunch of project config values. (These are
defined in the project's `devxhub_python.json`.)

Then, devxhub_python will generate a project from the template, using the values
that you entered. It will be placed in your current directory.

And if you want to specify a branch you can do that with::

    $ devxhub_python https://github.com/git-jamil/django-boilerplate.git --checkout develop

Works with private repos
------------------------

If you want to work with repos that are not hosted in github or bitbucket you can indicate explicitly the
type of repo that you want to use prepending `hg+` or `git+` to repo url::

    $ devxhub_python hg+https://example.com/repo

In addition, one can provide a path to the devxhub_python stored
on a local server::

    $ devxhub_python file://server/folder/project.git

Works with Zip files
--------------------

You can also distribute django-boilerplate templates as Zip files. To use a Zip file
template, point django-boilerplate at a Zip file on your local machine::

    $ devxhub_python /path/to/django-boilerplate.zip

Or, if the Zip file is online::

    $ devxhub_python https://example.com/path/to/django-boilerplate.zip

If the template has already been downloaded, or a template with the same name
has already been downloaded, you will be prompted to delete the existing
template before proceeding.

The Zip file contents should be the same as a git/hg repository for a template -
that is, the zipfile should unpack into a top level directory that contains the
name of the template. The name of the zipfile doesn't have to match the name of
the template - for example, you can label a zipfile with a version number, but
omit the version number from the directory inside the Zip file.

If you want to see an example Zipfile, find any django-boilerplate repository on Github
and download that repository as a zip file - Github repository downloads are in
a valid format for django-boilerplate.

Password-protected Zip files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your repository Zip file is password protected, devxhub_python will prompt you
for that password whenever the template is used.

Alternatively, if you want to use a password-protected Zip file in an
automated environment, you can export the `devxhub_python_REPO_PASSWORD`
environment variable; the value of that environment variable will be used
whenever a password is required.

Keeping your devxhub_pythons organized
------------------------------------

As of the devxhub_python 0.4.0 release:

* Whenever you generate a project with a devxhub_python, the resulting project
  is output to your current directory.

* Your cloned devxhub_pythons are stored by default in your `~/.devxhub_pythons/`
  directory (or Windows equivalent). The location is configurable: see
  :doc:`advanced/user_config` for details.

Pre-0.7.0, this is how it worked:

* Whenever you generate a project with a devxhub_python, the resulting project
  is output to your current directory.

* Cloned devxhub_pythons were not saved locally.
