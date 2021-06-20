from functools import wraps
from typing import Callable, Tuple, Any

from django_fsm import FSMField

from .entity import Entity


def save_and_refresh(wrapped_transition: Callable) -> Callable:
    @wraps(wrapped_transition)
    def _(process: Process, **kwargs):
        wrapped_transition(process, **kwargs)
        process.save(update_fields=('state',))
        return process

    return _


class Process(Entity):
    STATES: Tuple[Any, ...]
    state: FSMField

    class Meta:
        abstract = True
