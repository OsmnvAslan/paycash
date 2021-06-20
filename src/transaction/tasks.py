import requests
from celery import shared_task
from django.apps import apps

handled_exceptions = (requests.ConnectionError, requests.HTTPError,)


@shared_task(
    autoretry_for=handled_exceptions,
    retry_backoff=True, retry_kwargs={'max_retries': 8},
)
def update_transaction(transaction):
    pass
