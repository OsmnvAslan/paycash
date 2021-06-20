from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request


class CanDo(IsAuthenticated):
    app_label: str
    codename: str
    action: str
    method: str

    def has_permission(self, request: Request, view) -> bool:
        has_required_method: bool = request.method.lower() == self.method
        is_authenticated: bool = super().has_permission(
            request=request, view=view,
        )
        return is_authenticated and request.user.has_perm(
            perm=f'{self.app_label}.{self.action}_{self.codename}'
        ) if has_required_method else True


class CanRead(CanDo):
    action = 'view'
    method = 'get'


class CanCreate(CanDo):
    action = 'add'
    method = 'post'


class CanDelete(CanDo):
    action = 'delete'
    method = 'delete'


class CanUpdate(CanDo):
    action = 'change'
    method = 'patch'
