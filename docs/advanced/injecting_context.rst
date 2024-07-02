.. _injecting-extra-content:

Injecting Extra Context
-----------------------

You can specify an ``extra_context`` dictionary that will override values from ``devxhub_python.json`` or ``.devxhub_pythonrc``:

.. code-block:: python

    devxhub_python(
        'devxhub_python/',
        extra_context={'project_name': 'TheGreatest'},
    )

This works as command-line parameters as well:

.. code-block:: bash

    devxhub_python --no-input devxhub_python/ project_name=TheGreatest

You will also need to add these keys to the ``devxhub_python.json`` or ``.devxhub_pythonrc``.


Example: Injecting a Timestamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have ``devxhub_python.json`` that has the following keys:

.. code-block:: JSON

    {
        "timestamp": "{{ devxhub_python.timestamp }}"
    }


This Python script will dynamically inject a timestamp value as the project is
generated:

.. code-block:: python

    from devxhub_python.main import devxhub_python

    from datetime import datetime

    devxhub_python(
        'devxhub_python-django',
        extra_context={'timestamp': datetime.utcnow().isoformat()}
    )

How this works:

1. The script uses ``datetime`` to get the current UTC time in ISO format.
2. To generate the project, ``devxhub_python()`` is called, passing the timestamp
   in as context via the ``extra_context``` dict.
