.. _developmentguide:

Development Guide
=================

Please read our :ref:`Contributing guide lines <contributing>` first.

Requirements
------------

You can find any required library for this project in the *requirements.txt*:

.. literalinclude:: ../requirements.txt

NOTE: Make sure to have also all the extensions listed in the `docs/conf.py`_ that are required for the SDK Documentation.

.. _docs/conf.py: https://rawgit.com/hexonet/python-sdk/master/docs/conf.py

In addition, you need nodejs/npm with globally installed module *auto-changelog* in case you want to generate an update changelog version.
We suggest to use nvm_.

We suggest to use `Visual Studio Code`_ with installed plugins for Python Development described here_. But if you prefer any other IDE / Editor, it is fine.

.. _nvm: https://github.com/creationix/nvm
.. _Visual Studio Code: https://code.visualstudio.com
.. _here: https://code.visualstudio.com/docs/languages/python

.. _testsnvalidation:

Run Tests and Code Validation
-----------------------------

There are up to no automated tests realized, but planned to come in short.

Code validation and auto-fixing can be run by

.. code-block:: bash

    ./scripts/pep8fix.sh
    # to autofix possible issues

    ./scripts/pep9check.sh
    # to check for issues left

Please fix all issues before creating a PR.

Pull Request (PR) Procedure
---------------------------
* fork our project and create a new branch.
* clone it and check this branch out
* apply your desired changes / extensions
* :ref:`run tests and code validation<testsnvalidation>`
* commit and push it to remote
* open a pull request (PR)

**We care then about the rest** - no need to worry about things like building current realease and versioning. 

**You can stop here.**

The below sections are just for our reference.
TIA for your PR and thus for your support of this project. As we have further SDKs in other languages, it might take a bit of time to check if we can role out that PR as we want to keep all our SDKs aligned.

Versioning
----------

We use SemVer_ for versioning. For the versions available, see the `tags on this repository`_.

.. _SemVer: http://semver.org/
.. _tags on this repository: https://github.com/hexonet/python-sdk/tags

Releasing
---------

Merge the desired changes in case tests and code validation succeed.
Then create a new tag version by

.. code-block:: bash

    git tag -a v1.2.3 master
    # please replace the semver version accordingly

    git push --tags
    # push the tags to remote

Create a new release out of that new tag and provide release details about the changes applied in the `git interface`_. In case of breaking changes, describe what has changed and how to migrate.

.. _git interface: https://github.com/hexonet/python-sdk/releases

Changes will be auto-deployed by a webhook to readthedocs.org_ and automatically updated on `github pages`_.

.. _readthedocs.org: https://hexonet-python-sdk.readthedocs.io
.. _github pages: https://hexonet.github.io/python-sdk

Publish your changes to the Python Package Index (PyPi_) by

.. _PyPi: https://pypi.org/

.. code-block:: bash

    ./scripts/createdistribution.sh
    # to create packages of the new distribution

    ./scripts/uploaddistribution_test.sh
    # to upload the generated packages to the PyPi Test Index (test.pypi.org)

    ./scripts/uploaddistribution_live.sh
    # to upload the generated packages to the PyPi Index (pypi.org)

The module can be accessed on the `PyPi (Live) Index`_ and the `PyPi (Test) Index`_.

.. _PyPi (Live) Index: https://pypi.org/project/hexonet.apiconnector/
.. _PyPi (Test) Index: https://test.pypi.org/project/hexonet.apiconnector/

Generate SDK Documentation
--------------------------

Have an eye on the generated :ref:`api`.

If you want to generate it from scratch out of the sources, please use composer together with our project as follows:

.. code-block:: bash
    
    ./scripts/generatedocs.sh

The generated files are then available in subfolder "docs/_build/html". Commit and push the changes.

Update Changelog
----------------

After having changes merged and released, run

.. code-block:: bash
    
    ./scripts/changelog.sh

Commit and push the changes.