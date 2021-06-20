from typing import Tuple

DJANGO_APPS: Tuple[str, ...] = (
    'jazzmin', 'django.contrib.admin', 'django.contrib.staticfiles',
    'django.contrib.contenttypes', 'django.contrib.auth',
    'django.contrib.messages', 'django.contrib.sessions',
)
SIDE_APPS: Tuple[str, ...] = (
    'corsheaders', 'rest_framework', 'django_extensions',
    'django_filters', 'django_fsm', 'silk', 'graphene_django',
    'rest_framework.authtoken', 'solo', 'reversion',
)
PROJECT_APPS: Tuple[str, ...] = ('common', 'transaction')
message = 'No more than 5 apps per django project'
assert len(PROJECT_APPS) <= 5, message  # nosec
DEFAULT_APPS: Tuple[str, ...] = DJANGO_APPS + SIDE_APPS + PROJECT_APPS
