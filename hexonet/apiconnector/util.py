import re
import time
import base64
from six.moves.urllib.parse import quote, unquote
from datetime import datetime


def command_encode(command):
    """
    Encode the command array in a command-string
    .. versionadded:: 1.0.0
    """
    return "\n".join(_command_encode(command))


def _command_encode(command):
    r = []

    if isinstance(command, int):
        command = str(command)
    if isinstance(command, str):
        return ["=" + command]
    elif isinstance(command, dict):
        for k, v in command.items():
            for v2 in _command_encode(v):
                r.append(k.upper() + v2)
    elif isinstance(command, list):
        for (i, v) in enumerate(command):
            for v2 in _command_encode(v):
                r.append(str(i) + v2)
    else:
        pass

    return r


def response_to_hash(response):
    """
    Convert the response string as a hash
    .. versionadded:: 1.0.0
    """
    r = {'PROPERTY': {}}
    re1 = re.compile(r'^([^\=]*[^\t\= ])[\t ]*=[\t ]*(.*)')
    re2 = re.compile(r'^property\[([^\]]*)\]', re.IGNORECASE)
    for line in response.split("\n"):
        m1 = re1.match(line)
        if not m1:
            continue
        attr = m1.group(1)
        value = m1.group(2)
        value = re.sub(r'[\t ]*$', '', value)

        m2 = re2.match(attr)
        if m2:
            prop = m2.group(1).upper()
            prop = re.sub(r'\s', '', prop)
            if prop not in r['PROPERTY']:
                r['PROPERTY'][prop] = []
            r['PROPERTY'][prop].append(value)
        else:
            r[attr.upper()] = value

    if 'CODE' in r:
        r['CODE'] = int(r['CODE'])
    if 'RUNTIME' in r:
        r['RUNTIME'] = float(r['RUNTIME'])
    if 'QUEUETIME' in r:
        r['QUEUETIME'] = float(r['QUEUETIME'])
    return r


def response_to_list_hash(response):
    """
    Convert the response string as a list hash
    .. versionadded:: 1.0.0
    """
    list_hash = {
        'CODE': "",
        'DESCRIPTION': "",
        'RUNTIME': "",
        'QUEUETIME': "",
        'ITEMS': []
    }

    if 'CODE' in response:
        list_hash['CODE'] = response['CODE']
    if 'DESCRIPTION' in response:
        list_hash['DESCRIPTION'] = response['DESCRIPTION']
    if 'RUNTIME' in response:
        list_hash['RUNTIME'] = response['RUNTIME']
    if 'QUEUETIME' in response:
        list_hash['QUEUETIME'] = response['QUEUETIME']

    count = 0
    if 'PROPERTY' in response:
        columns = None
        if 'COLUMN' in response['PROPERTY']:
            list_hash['COLUMNS'] = response['PROPERTY']['COLUMN']
            columns = {}
            for col in list_hash['COLUMNS']:
                columns[col] = 1
        else:
            list_hash['COLUMNS'] = []

        for prop, values in response['PROPERTY'].items():
            if prop == "COLUMN":
                continue
            if prop in ['FIRST', 'LAST', 'LIMIT', 'COUNT', 'TOTAL']:
                list_hash[prop] = int(response['PROPERTY'][prop][0])
            else:
                # if columns and not columns[prop]:
                #    continue
                list_hash['COLUMNS'].append(prop)
                index = 0
                for v in values:
                    if index >= len(list_hash['ITEMS']):
                        list_hash['ITEMS'].append({})
                    list_hash['ITEMS'][index][prop] = v
                    index = index + 1
                if index > count:
                    count = index

    if 'COUNT' not in list_hash:
        list_hash['COUNT'] = count
    if 'FIRST' not in list_hash:
        list_hash['FIRST'] = 0
    if 'TOTAL' not in list_hash:
        list_hash['TOTAL'] = list_hash['COUNT']

    if 'FIRST' in list_hash and 'LIMIT' in list_hash and list_hash['LIMIT'] > 0:
        list_hash['PAGE'] = int(list_hash['FIRST'] / list_hash['LIMIT']) + 1
        if list_hash['PAGE'] > 1:
            list_hash['PREVPAGE'] = list_hash['PAGE'] - 1
            list_hash['PREVPAGEFIRST'] = (list_hash['PREVPAGE'] - 1) * list_hash['LIMIT']
        list_hash['NEXTPAGE'] = list_hash['PAGE'] + 1
        list_hash['NEXTPAGEFIRST'] = (list_hash['NEXTPAGE'] - 1) * list_hash['LIMIT']

    if 'TOTAL' in list_hash and 'LIMIT' in list_hash and list_hash['LIMIT'] > 0:
        list_hash['PAGES'] = int(list_hash['TOTAL'] + list_hash['LIMIT'] - 1) / list_hash['LIMIT']
        list_hash['LASTPAGEFIRST'] = (list_hash['PAGES'] - 1) * list_hash['LIMIT']
        if 'NEXTPAGE' in list_hash and (list_hash['NEXTPAGE'] > list_hash['PAGES']):
            list_hash['NEXTPAGE'] = None
            list_hash['NEXTPAGEFIRST'] = None

    return list_hash


def sqltime(timestamp=None):
    """
    Convert the Unix-Timestamp to a SQL datetime
    If no timestamp given, returns the current datetime
    .. versionadded:: 1.0.0
    """
    if timestamp:
        return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def timesql(sqldatetime):
    """
    Convert the SQL datetime to Unix-Timestamp
    .. versionadded:: 1.0.0
    """
    return int(time.mktime(datetime.strptime(sqldatetime, '%Y-%m-%d %H:%M:%S').timetuple()))


def url_encode(string):
    """
    URL-encodes string
    This function is convenient when encoding a string to be used in a query
    part of a URL
    .. versionadded:: 1.0.0
    """
    return quote(string)


def url_decode(string):
    """
    Decodes URL-encoded string Decodes any %## encoding in the given string.
    .. versionadded:: 1.0.0
    """
    return unquote(string)


def base64_encode(string):
    """
    Encodes data with MIME base64
    This encoding is designed to make binary data survive transport through transport layers that
    are not 8-bit clean, such as mail bodies.
    parameter: musst be bytes not str for python3 at least
    e.g. base64_encode(b"some string")
    .. versionadded:: 1.0.0
    """
    return base64.b64encode(string)


def base64_decode(string):
    """
    Decodes data encoded with MIME base64
    parameter: musst be bytes not str for python3 at least
    e.g. base64_decode(b"ZGFzIHN0aW5rdCB6dW0gSGltbWVs")
    .. versionadded:: 1.0.0
    """
    return base64.b64decode(string)
