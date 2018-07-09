from hexonet.apiconnector import Connection
from hexonet.apiconnector import Response

__version__ = '1.2.1'
name = "hexonet.apiconnector"


def connect(login=None, password=None, url=None, entity=None, user=None, role=None, config=None):
    """
    Returns an instance of hexonet.apiconnector.Connection
    """

    if config is None:
        config = {}
    if login is not None:
        config['login'] = login
    if password is not None:
        config['password'] = password
    if url is not None:
        config['url'] = url
    if entity is not None:
        config['entity'] = entity
    if user is not None:
        config['user'] = user
    if role is not None:
        config['role'] = role
    return Connection(config)
