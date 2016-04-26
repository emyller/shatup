import pytest

from backend.url_parser import parse_url


def test_parse_url_raises_if_invalid_url():
    """`parse_url` raises ValueError when receiving an invalid URL
    """
    with pytest.raises(ValueError):
        parse_url('invalid url')

def test_parse_url_handles_url_with_hostname_only():
    """`parse_url` works well when provided only: hostname
    """
    parsed_url = parse_url('redis://localhost')
    expected = {
        'protocol': 'redis',
        'hostname': 'localhost',
    }
    assert expected.items() < set(parsed_url.items())

def test_parse_url_handles_url_with_hostname_and_port_only():
    """`parse_url` works well when provided only: hostname, port
    """
    parsed_url = parse_url('redis://localhost:6379')
    expected = {
        'protocol': 'redis',
        'hostname': 'localhost',
        'port': '6379',
    }
    assert expected.items() < set(parsed_url.items())

def test_parse_urL_handles_url_with_authentication_info():
    """`parse_url` works well when provided only: hostname, username, password
    """
    parsed_url = parse_url('redis://root:undiscl0sed@localhost:6379')
    expected = {
        'protocol': 'redis',
        'hostname': 'localhost',
        'username': 'root',
        'password': 'undiscl0sed',
    }
    assert expected.items() < set(parsed_url.items())

def test_parse_url_handles_url_with_empty_password():
    """`parse_url` works well when provided only: hostname, username
    """
    parsed_url = parse_url('redis://root:@localhost:6379')
    expected = {
        'protocol': 'redis',
        'hostname': 'localhost',
        'username': 'root',
        'password': '',
    }
    assert expected.items() < set(parsed_url.items())

def test_parse_url_handles_url_with_path():
    """`parse_url` works well when provided only: hostname, path
    """
    parsed_url = parse_url('redis://localhost/somewhere')
    expected = {
        'protocol': 'redis',
        'hostname': 'localhost',
        'path': '/somewhere',
    }
    assert expected.items() < set(parsed_url.items())

def test_parse_url_handles_full_featured_url():
    """`parse_url` works well when provided every expected component
    """
    parsed_url = parse_url('redis://root:undiscl0sed@localhost:6379/somewhere')
    expected = {
        'protocol': 'redis',
        'hostname': 'localhost',
        'port': '6379',
        'username': 'root',
        'password': 'undiscl0sed',
        'path': '/somewhere',
    }
    assert expected == parsed_url
