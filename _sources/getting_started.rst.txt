.. _getting_started_reference-label:

===============
Getting started
===============
----------
Installing
----------
Make sure to have python >= 3.8 installed.

1. Installing the package builder
.. code-block:: bash
    python3 -m pip install --upgrade build
2. Building
.. code-block:: bash
    python3 -m build

3. Installing the assembled package
.. code-block:: bash
    python -m pip install -e .

4. Installing external dependencies
.. code-block:: bash
    pip install -r requirements.txt