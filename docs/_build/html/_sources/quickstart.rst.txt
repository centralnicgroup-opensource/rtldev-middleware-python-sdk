.. _quickstart:

Quickstart
==========

Eager to get started?  This page gives a good introduction to hexonet.apiconnector.
It assumes you already have it installed. If you do not, head over to the
:ref:`installation` section.


A Minimal Application
---------------------

A minimal application using hexonet.apiconnector looks something like this:

.. literalinclude:: app.py
    :language: python
    :encoding: utf-8
    :caption: Python SDK Demo App   

So what did that code do?

1. First we imported the :mod:`hexonet.apiconnector`.

2. Next we create an Connection to the HEXONET Backend System by using the :meth:`~hexonet.apiconnector.connect`.

3. We then use the :meth:`~hexonet.apiconnector.connection.Connection.call` to request a provided command to the backend system.

4. The response is an instance of :class:`~hexonet.apiconnector.response.Response`. It provides all necessary methods to access API response data.

What to do if the backend system just returns an error
------------------------------------------------------

Well this in general needs some further analysis. Reasons might be that you have an ip filter defined and you do not provide your ip address through configuration option "remoteaddr".
It could also be that you provided an ip address that is blocked.
Another issue can be that you connect using a role user that is not allowed to request this command as it got blocked by role user configuration.

Feel free to :ref:`contact-us` if you need help.

Sessions
--------

Session-based communication is not yet available in this SDK. This is a planned rewrite.
The above application code shows how sessionless communication with the HEXONET Backend API works.