.. _suppressing-command-line-prompts:

Suppressing Command-Line Prompts
--------------------------------

To suppress the prompts asking for input, use ``no_input``.

Note: this option will force a refresh of cached resources.

Basic Example: Using the Defaults
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

devxhub_python will pick a default value if used with ``no_input``:

.. code-block:: python

    from devxhub_python.main import devxhub_python
    devxhub_python(
        'devxhub_python-django',
        no_input=True,
    )

In this case it will be using the default defined in ``devxhub_python.json`` or ``.devxhub_pythonrc``.

.. note::
   values from ``devxhub_python.json`` will be overridden by values from  ``.devxhub_pythonrc``

Advanced Example: Defaults + Extra Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you combine an ``extra_context`` dict with the ``no_input`` argument, you can programmatically create the project with a set list of context parameters and without any command line prompts:

.. code-block:: python

    devxhub_python('devxhub_python/',
                 no_input=True,
                 extra_context={'project_name': 'TheGreatest'})


See also :ref:`injecting-extra-content` and the :ref:`API Reference <apiref>` for more details.
