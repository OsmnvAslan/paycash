from django.contrib.auth.models import User, Permission
from django.test import Client
from pytest import fixture
from responses import RequestsMock
from rest_framework.authtoken.models import Token


@fixture
def authenticated_client(client: Client) -> Client:
    user = User.objects.create_user(
        username='username', password='password',
    )
    permissions = Permission.objects.all()
    user.user_permissions.set(permissions)
    token, _ = Token.objects.get_or_create(user=user)
    headers = {
        'HTTP_AUTHORIZATION': f'Token {token.key}',
    }
    client.defaults.update(**headers)
    return client


@fixture
def mocked_zvonobot_response_for_record():
    with RequestsMock() as responses_mock:
        responses_mock.add(
            url='https://lk.zvonobot.kz/apiCalls/createRecord',
            method=responses_mock.POST, status=200,
            json={
                'data': {
                    'id': 661923, 'createdAt': 123123123,
                    'needModeration': 1, 'moderatorComment': '',
                    'name': '', 'path': '', 'status': '', 'recordText': '',
                },
            },
        )
        yield responses_mock
