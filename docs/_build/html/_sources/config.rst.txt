.. _config:

Configuration Handling
======================

Applications need some kind of configuration. There are different settings
you might want to change depending on the application environment like
toggling the debug mode, setting credentials etc.

The way hexonet.apiconnector is designed usually requires the configuration
to be provided at runtime when connecting to the HEXONET Backend API. You
can hardcode the configuration in the code, which for many small scripts is
for sure sufficient. Realtime applications and frontends need to cover some
application logic around using this SDK like a login form and session
management.


Configuration Basics
--------------------

The configuration can be provided in two ways.
Using the :class:`~hexonet.apiconnector.APIClient`:

.. literalinclude:: app.py
    :language: python
    :encoding: utf-8
    :caption: Python SDK Demo App

Environment and Debug Features
------------------------------

Debug Features are also available in our Python SDK::

    # activate debug mode
    cl.enableDebugMode()

    # disable debug mode
    cl.disableDebugMode()

HEXONET provides two different Backend Systems that you might consider to use.
Both require a separate Registration:
- `Live System Registration <https://www.hexonet.net/sign-up>`_ and
- `OT&E System Registration <https://www.hexonet.net/signup-ote>`_.

OT&E System
^^^^^^^^^^^

OT&E Sytem stands for Operational Test & Evaluation System.
No costs, just for playing around with things. This system can be seen as a
kind of sandbox system that allows to test your integration first before going
live with it. This system and the use of our products and services is
completely free of charge.
To use this system, use APIClient's method `cl.useOTESystem()`.
Otherwise Live System will be used by default.

LIVE System
^^^^^^^^^^^

The real world system - This system and the use our services and products can
lead to real costs depending on what you're exactly doing.
Live System will be used by default, but you can also use APIClient's method
`cl.useLIVESystem()` to add it in source code for reference.

Builtin Configuration Values
----------------------------

The following configuration values are used internally by hexonet.apiconnector:

Up to now - none, but this might change in future as we are continously
improving our SDKs.
