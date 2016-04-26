"""
A custom URL parser intended to break a 12factor-like URL into a dict.
"""
import re


RE_URL = re.compile(r'''
    (?P<protocol>[a-z0-9]+)://  # Protocol
    (?:(?P<username>[\w-]+):(?P<password>.*)@)?  # Authentication
    (?P<hostname>[^:/$]+)(?::(?P<port>\d+))?  # Hostname and port
    (?P<path>.*)?  # Path
''', re.VERBOSE)


def parse_url(url):
    """Parse a 12factor-like URL into a dict
    """
    parsed_url = RE_URL.match(url)

    if not parsed_url:
        raise ValueError('Invalid URL: {}'.format(url))

    return parsed_url.groupdict()
