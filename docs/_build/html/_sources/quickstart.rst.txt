.. _quickstart:

Quickstart
==========

Eager to get started?  This page gives a good introduction to
hexonet.apiconnector. It assumes you already have it installed.
If you do not, head over to the :ref:`installation` section.


A Minimal Application
---------------------

A minimal application using hexonet.apiconnector looks something like follows.
We provided two short examples: one for sessionless communication and one for
session-based communication.

.. literalinclude:: app.py
    :language: python
    :encoding: utf-8
    :caption: Python SDK Demo App

You can find this code also on github_.

.. _github: https://github.com/hexonet/python-sdk-demo

What to do if the backend system just returns an error
------------------------------------------------------

Well this in general needs some further analysis. Reasons might be that you
have an ip filter defined and you do not provide your ip address through
configuration option "remoteaddr".
It could also be that you provided an ip address that is blocked.
Another issue can be that you connect using a role user that is not allowed
to request this command as it got blocked by role user configuration.

Feel free to :ref:`contact-us` if you need help.

Sessions
--------

Session-based communication is available in this SDK, see above.
Use :meth:`~hexonet.apiconnector.apiclient.APIClient.saveSession` and
:meth:`~hexonet.apiconnector.apiclient.APIClient.reuseSession` if you
plan to build your own frontend on top using session handling.
