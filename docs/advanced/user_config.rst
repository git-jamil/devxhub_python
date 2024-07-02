.. _user-config:

User Config
===========

*New in devxhub_python 0.7*

If you use devxhub_python a lot, you'll find it useful to have a user config file.
By default devxhub_python tries to retrieve settings from a `.devxhub_pythonrc` file in your home directory.

*New in devxhub_python 1.3*

You can also specify a config file on the command line via ``--config-file``.

.. code-block:: bash

    devxhub_python --config-file /home/audreyr/my-custom-config.yaml devxhub_python

Or you can set the ``devxhub_python_CONFIG`` environment variable:

.. code-block:: bash

    export devxhub_python_CONFIG=/home/audreyr/my-custom-config.yaml

If you wish to stick to the built-in config and not load any user config file at all, use the CLI option ``--default-config`` instead.
Preventing devxhub_python from loading user settings is crucial for writing integration tests in an isolated environment.

Example user config:

.. code-block:: yaml

    default_context:
        full_name: "Audrey Roy"
        email: "audreyr@example.com"
        github_username: "audreyr"
    devxhub_pythons_dir: "/home/audreyr/my-custom-devxhub_pythons-dir/"
    replay_dir: "/home/audreyr/my-custom-replay-dir/"
    abbreviations:
        pp: https://github.com/devxhub/devxhub_python.git
        gh: https://github.com/{0}.git
        bb: https://bitbucket.org/{0}

Possible settings are:

``default_context``:
    A list of key/value pairs that you want injected as context whenever you generate a project with devxhub_python.
    These values are treated like the defaults in ``devxhub_python.json``, upon generation of any project.
``devxhub_pythons_dir``
    Directory where your devxhub_pythons are cloned to when you use devxhub_python with a repo argument.
``replay_dir``
    Directory where devxhub_python dumps context data to, which you can fetch later on when using the
    :ref:`replay feature <replay-feature>`.
``abbreviations``
    A list of abbreviations for devxhub_pythons.
    Abbreviations can be simple aliases for a repo name, or can be used as a prefix, in the form ``abbr:suffix``.
    Any suffix will be inserted into the expansion in place of the text ``{0}``, using standard Python string formatting.
    With the above aliases, you could use the ``devxhub_python`` template simply by saying ``devxhub_python pp``, or ``devxhub_python gh:audreyr/devxhub_python``.
    The ``gh`` (GitHub), ``bb`` (Bitbucket), and ``gl`` (Gitlab) abbreviations shown above are actually **built in**, and can be used without defining them yourself.

Read also: :ref:`injecting-extra-content`
