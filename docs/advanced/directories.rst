.. _directories:

Organizing devxhub_pythons in directories
---------------------------------------

*New in devxhub_python 1.7*

devxhub_python introduces the ability to organize several templates in one repository or zip file, separating them by directories.
This allows using symlinks for general files.
Here's an example repository demonstrating this feature::

    https://github.com/user/repo-name.git
        ├── directory1-name/
        |   ├── {{devxhub_python.project_slug}}/
        |   └── devxhub_python.json
        └── directory2-name/
            ├── {{devxhub_python.project_slug}}/
            └── devxhub_python.json

To activate one of templates within a subdirectory, use the ``--directory`` option:

.. code-block:: bash

    devxhub_python https://github.com/user/repo-name.git --directory="directory1-name"
