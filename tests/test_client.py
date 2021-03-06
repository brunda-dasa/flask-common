from __future__ import (
    print_function,
    absolute_import,
    division,
    unicode_literals,
)

from flask_common.client import ApiClient
from flask import Flask
from werkzeug.datastructures import Headers


def test_api_client_basic_auth():
    app = Flask('test')
    client = ApiClient(app, api_key='123456')

    headers = client.get_headers(client.api_key)
    assert headers == Headers([('Authorization', 'Basic MTIzNDU2Og==',)])
