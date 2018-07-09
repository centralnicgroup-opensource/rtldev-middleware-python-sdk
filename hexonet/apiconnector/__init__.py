from apiconnector.connection import Connection
from apiconnector.response import Response

__version__ = '1.0.0'
name = "apiconnector"

def connect(login=None, password=None, url=None, entity=None, user=None, role=None, config=None):
	"""
	Returns an instance of apiconnector.Connection
	"""

	if config == None:
		config = {}
	if login != None:
		config['login'] = login
	if password != None:
		config['password'] = password
	if url != None:
		config['url'] = url
	if entity != None:
		config['entity'] = entity
	if user != None:
		config['user'] = user
	if role != None:
		config['role'] = role
	return Connection(config)

