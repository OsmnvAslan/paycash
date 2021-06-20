from typing import Tuple

from reversion import register
from .entity import Entity
from .global_configuration import GlobalConfiguration
from .process import Process, save_and_refresh
from .profile import Profile
from .company import Company

register(model=GlobalConfiguration, format='json')
register(model=Profile, format='json')
register(model=Company, format='json')

__all__: Tuple = (
    'Entity', 'Process', 'save_and_refresh', 'Profile',
    'GlobalConfiguration', 'Company',
)
