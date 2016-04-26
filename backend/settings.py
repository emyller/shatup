from unipath import Path


# Basic (self-explanatory) definitions
BASE_DIR = Path(__file__).ancestor(2)


# Muffin plug-ins
PLUGINS = [
    'muffin_jade',
]

# Important directories
STATIC_FOLDERS = [
    BASE_DIR.child('frontend', 'static'),
    BASE_DIR.child('frontend', 'bower_components'),
]
JADE_TEMPLATE_FOLDERS = [
    BASE_DIR.child('frontend', 'templates'),
]
