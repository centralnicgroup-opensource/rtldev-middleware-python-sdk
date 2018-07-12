Upgrading to Newer Releases
===========================

hexonet.apiconnector itself is changing like any software is changing over time.
Most of the changes are the nice kind, the kind where you don't have to change
anything in your code to profit from a new release. These are in general changes that
are released as patch or minor release.

However every once in a while there are changes that do require some
changes in your code or there are changes that make it possible for you to
improve your own code quality by taking advantage of new features in
hexonet.apiconnector. Such breaking changes are covered through major releases.

Use the :command:`pip` command to upgrade your existing hexonet.apiconnector installation by
providing the ``--upgrade`` parameter::

    $ pip install --upgrade hexonet.apiconnector
    # for python 2.x

    $ pip3 install --upgrade hexonet.apiconnector
    # for python 3.x

See the how to migrate your code by reading the `release notes`_.
We publish there any information on how to migrate.

.. _release notes: https://github.com/hexonet/python-sdk/releases