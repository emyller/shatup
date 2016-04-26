from unipath import Path
from decouple import config as read_conf  # `config` clashes with Muffin

from backend.url_parser import parse_url


# Basic (self-explanatory) definitions
BASE_DIR = Path(__file__).ancestor(2)

# Muffin plug-ins
PLUGINS = [
    'muffin_jade',
    'muffin_redis',
]

# Important directories
STATIC_FOLDERS = [
    BASE_DIR.child('frontend', 'static'),
    BASE_DIR.child('frontend', 'bower_components'),
]
JADE_TEMPLATE_FOLDERS = [
    BASE_DIR.child('frontend', 'templates'),
]

# Redis database
REDIS_URL = read_conf('REDIS_URL', 'redis://localhost/0', parse_url)
REDIS_HOST = REDIS_URL['hostname']
REDIS_PORT = REDIS_URL['port']
REDIS_PASSWORD = REDIS_URL['password']
REDIS_DB = int(REDIS_URL['path'][1:])
