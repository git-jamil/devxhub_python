.. _templates:

Templates inheritance (0.0.2+)
---------------------------------------------------

*New in devxhub_python 0.0.2+*

Sometimes you need to extend a base template with a different
configuration to avoid nested blocks.

devxhub_python introduces the ability to use common templates
using the power of jinja: `extends`, `include` and `super`.

Here's an example repository::

    https://github.com/user/repo-name.git
    ├── {{devxhub_python.project_slug}}/
    |   └── file.txt
    ├── templates/
    |   └── base.txt
    └── devxhub_python.json

every file in the `templates` directory will become referable inside the project itself,
and the path should be relative from the `templates` folder like ::

    # file.txt
    {% extends "base.txt" %}

    ... or ...

    # file.txt
    {% include "base.txt" %}

see more on https://jinja.palletsprojects.com/en/2.11.x/templates/
