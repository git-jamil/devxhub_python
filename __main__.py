"""Allow devxhub_python to be executable from a checkout or zip file."""

import runpy

if __name__ == "__main__":
    runpy.run_module("devxhub_python", run_name="__main__")
