# python-sdk

[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
[![Build Status](https://travis-ci.com/hexonet/python-sdk.svg?branch=master)](https://travis-ci.com/hexonet/python-sdk)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hexonet.apiconnector.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/hexonet.apiconnector.svg)](https://pypi.org/project/hexonet.apiconnector/)
[![Documentation Status](https://readthedocs.org/projects/hexonet-python-sdk/badge/?version=latest)](https://hexonet-python-sdk.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/hexonet/python-sdk/blob/master/CONTRIBUTING.md)

This module is a connector library for the insanely fast HEXONET Backend API. For further informations visit our [homepage](http://hexonet.net) and do not hesitate to [contact us](https://www.hexonet.net/contact).

## Resources

* [Usage Guide](https://hexonet-python-sdk.readthedocs.io/en/latest/#usage-guide)
* [SDK Documentation](https://hexonet-python-sdk.readthedocs.io/en/latest/#sdk-documentation)
* [HEXONET Backend API Documentation](https://github.com/hexonet/hexonet-api-documentation/tree/master/API)
* [Release Notes](https://github.com/hexonet/python-sdk/releases)
* [Development Guide](https://hexonet-python-sdk.readthedocs.io/en/latest/developmentguide.html)

## Features

* Automatic IDN Domain name conversion to punycode (our API accepts only punycode format in commands)
* Allows nested associative arrays in API commands to improve for bulk parameters
* Connecting and communication with our API
* Several ways to access and deal with response data
* Getting the command again returned together with the response
* Sessionless communication
* Session based communication
* Possibility to save API session identifier in PHP session
* Configure a Proxy for API communication
* Configure a Referer for API communication
* High Performance Proxy Setup

### High Performance Proxy Setup

Long distances to our main data center in Germany may result in high network latencies. If you encounter such problems, we highly recommend to use this setup, as it uses persistent connections to our API server and the overhead for connection establishments is omitted.

#### Step 1: Required Apache2 packages / modules

*At least Apache version 2.2.9* is required.

The following Apache2 modules must be installed and activated:

```bash
proxy.conf
proxy.load
proxy_http.load
ssl.conf # for HTTPs connection to our API server
ssl.load # for HTTPs connection to our API server
```

#### Step 2: Apache configuration

An example Apache configuration with binding to localhost:

```bash
<VirtualHost 127.0.0.1:80>
    ServerAdmin webmaster@localhost
    ServerSignature Off
    SSLProxyEngine on
    ProxyPass /api/call.cgi https://api.ispapi.net/api/call.cgi min=1 max=2
    <Proxy *>
        Order Deny,Allow
        Deny from none
        Allow from all
    </Proxy>
</VirtualHost>
```

After saving your configuration changes please restart the Apache webserver.

#### Step 3: Using this setup

```python
from hexonet.apiconnector.apiclient import APIClient as AC

cl = AC()
cl.useOTESystem()
cl.useHighPerformanceConnectionSetup() # Default Connection Setup would be used otherwise by default
cl.setCredentials('test.user', 'test.passw0rd')
r = cl.request({"COMMAND" => "StatusAccount"})
```

So, what happens in code behind the scenes? We communicate with localhost (so our proxy setup) that passes the requests to the HEXONET API.
Of course we can't activate this setup by default as it is based on Steps 1 and 2. Otherwise connecting to our API wouldn't work.

Just in case the above port or ip address can't be used, use function setURL instead to set a different URL / Port.
`http://127.0.0.1/api/call.cgi` is the default URL for the High Performance Proxy Setup.
e.g. `$cl->setURL("http://127.0.0.1:8765/api/call.cgi");` would change the port. Configure that port also in the Apache Configuration (-> Step 2)!

Don't use `https` for that setup as it leads to slowing things down as of the https `overhead` of securing the connection. In this setup we just connect to localhost, so no direct outgoing network traffic using `http`. The apache configuration finally takes care passing it to `https` for the final communication to the HEXONET API.

## How to use this module in your project

All you need to know, can be found [here](https://hexonet-python-sdk.readthedocs.io/en/latest/#usage-guide).

## Contributing

Please read [our development guide](https://hexonet-python-sdk.readthedocs.io/en/latest/developmentguide.html) for details on our code of conduct, and the process for submitting pull requests to us.

```bash
pip3 install -e .
```

## Authors

List of responsible developers can be found [here](https://github.com/hexonet/python-sdk/blob/master/AUTHORS.md)

See also the list of [contributors](https://github.com/hexonet/php-sdk/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
