.. _calling-from-python:

Calling devxhub_python Functions From Python
------------------------------------------

You can use devxhub_python from Python:

.. code-block:: python

    from devxhub_python.main import devxhub_python

    # Create project from the devxhub_python/ template
    devxhub_python('devxhub_python/')

    # Create project from the devxhub_python.git repo template
    devxhub_python('https://github.com/devxhub/devxhub_python.git')

This is useful if, for example, you're writing a web framework and need to provide developers with a tool similar to `django-admin.py startproject` or `npm init`.

See the :ref:`API Reference <apiref>` for more details.
