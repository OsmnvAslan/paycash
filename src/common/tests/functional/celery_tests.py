from django.conf import settings
from responses import RequestsMock

from ...tasks import (
    send_message_via_infobip, call_via_zvonobot,
)


def test_send_message_via_infobip() -> None:
    with RequestsMock() as requests_mock:
        requests_mock.add(
            method=requests_mock.POST, url=settings.INFOBIP_URL,
        )
        send_message_via_infobip(to='77071367581', text='')


def test_send_message_via_zvonobot() -> None:
    with RequestsMock() as requests_mock:
        requests_mock.add(
            method=requests_mock.POST,
            url=f'{settings.ZVONOBOT_BASE_URL}create',
        )
        call_via_zvonobot(to='77071367581', record_id=0)
