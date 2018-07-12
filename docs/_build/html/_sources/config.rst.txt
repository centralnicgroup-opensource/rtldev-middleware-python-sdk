.. _config:

Configuration Handling
======================

Applications need some kind of configuration. There are different settings
you might want to change depending on the application environment like
toggling the debug mode, setting credentials etc.

The way hexonet.apiconnector is designed usually requires the configuration to be
provided at runtime when connecting to the HEXONET Backend API. You can hardcode 
the configuration in the code, which for many small scripts is for sure sufficient.
Realtime applications and frontends need to cover some application logic around 
using this SDK like a login form and session management.


Configuration Basics
--------------------

The configuration can be provided in two ways.
Using the :meth:`hexonet.apiconnector.connect`::
        
    import hexonet.apiconnector
    api = hexonet.apiconnector.connect(
        "test.user",
        "test.passw0rd",
        "https://coreapi.1api.net/api/call.cgi",
        "1234"
        //,"hexotestman.com" //subuser view
        //,"testrole" //specify a role user
    );

or by using the :class:`hexonet.apiconnector.connection.Connection` class accordingly::

    from hexonet.apiconnector.connection import Connection as HXClient
    api = HXClient({
        "login": "test.user",
        "password": "test.passw0rd",
        "url": "https://coreapi.1api.net/api/call.cgi",
        "entity": "1234",    
        //"user": "hexotestman.com",//subuser view
        //"role": "testrole",//specify a role user
    });


Environment and Debug Features
------------------------------

HEXONET provides two different Backend Systems that you might consider to use:

- Operational Test & Evaluation (OT&E) System (set 'entity' to '1234')
No costs, just for playing around with things. This system can be seen as a
kind of sandbox system that allows to test your integration first before going
live with it. This system and the use of our products and services is completely
free of charge.

- LIVE System (set 'entity' to '54cd')
The real world system - This system and the use our services and products can lead
to real costs depending on what you're exactly doing.

Both systems need a separate registration_ first.

.. _registration: https://www.hexonet.net

Debug Features, are up to now not available at the hexonet.apiconnector, but planned.


Builtin Configuration Values
----------------------------

The following configuration values are used internally by hexonet.apiconnector:

Up to now - none, but this might change in future as we are continously improving our SDKs.