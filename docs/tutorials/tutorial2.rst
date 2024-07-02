.. _tutorial2:

==================================
Create a devxhub_python From Scratch
==================================

In this tutorial, we are creating `devxhub_python-website-simple`, a devxhub_python for generating simple, bare-bones websites.

Step 1: Name Your devxhub_python
------------------------------

Create the directory for your devxhub_python and cd into it:

.. code-block:: bash

    $ mkdir devxhub_python-website-simple
    $ cd devxhub_python-website-simple/

Step 2: Create devxhub_python.json
----------------------------------

`devxhub_python.json` is a JSON file that contains fields which can be referenced in the devxhub_python template. For each, default value is defined and user will be prompted for input during devxhub_python execution. Only mandatory field is `project_slug` and it should comply with package naming conventions defined in `PEP8 Naming Conventions <https://www.python.org/dev/peps/pep-0008/#package-and-module-names>`_ .

.. code-block:: json

    {
      "project_name": "devxhub_python Website Simple",
      "project_slug": "{{ devxhub_python.project_name.lower().replace(' ', '_') }}",
      "author": "Anonymous"
    }


Step 3: Create project_slug Directory
---------------------------------------

Create a directory called `{{ devxhub_python.project_slug }}`.

This value will be replaced with the repo name of projects that you generate from this devxhub_python.

Step 4: Create index.html
--------------------------

Inside of `{{ devxhub_python.project_slug }}`, create `index.html` with following content:

.. code-block:: html

    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>{{ devxhub_python.project_name }}</title>
        </head>

        <body>
            <h1>{{ devxhub_python.project_name }}</h1>
            <p>by {{ devxhub_python.author }}</p>
        </body>
    </html>

Step 5: Pack devxhub_python into ZIP
----------------------------------
There are many ways to run devxhub_python templates, and they are described in details in `Usage chapter <https://devxhub_python.readthedocs.io/en/latest/usage.html#grab-a-devxhub_python-template>`_. In this tutorial we are going to ZIP devxhub_python and then run it for testing.

By running following command `devxhub_python.zip` will get generated which can be used to run devxhub_python. Script will generate `devxhub_python.zip` ZIP file and echo full path to the file.

.. code-block:: bash

   $ (SOURCE_DIR=$(basename $PWD) ZIP=devxhub_python.zip && # Set variables
   pushd .. && # Set parent directory as working directory
   zip -r $ZIP $SOURCE_DIR --exclude $SOURCE_DIR/$ZIP --quiet && # ZIP devxhub_python
   mv $ZIP $SOURCE_DIR/$ZIP && # Move ZIP to original directory
   popd && # Restore original work directory
   echo  "devxhub_python full path: $PWD/$ZIP")

Step 6: Run devxhub_python
------------------------
Set your work directory to whatever directory you would like to run devxhub_python at. Use devxhub_python full path and run the following command:

.. code-block:: bash

   $ devxhub_python <replace with devxhub_python full path>

You can expect similar output:

.. code-block:: bash

   $ devxhub_python /Users/admin/devxhub_python-website-simple/devxhub_python.zip
   project_name [devxhub_python Website Simple]: Test web
   project_slug [test_web]:
   author [Anonymous]: devxhub_python Developer

Resulting directory should be inside your work directory with a name that matches `project_slug` you defined. Inside that directory there should be `index.html` with generated source:

.. code-block:: html

    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Test web</title>
        </head>

        <body>
            <h1>Test web</h1>
            <p>by devxhub_python Developer</p>
        </body>
    </html>
