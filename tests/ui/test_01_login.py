import os
import json
import pytest
from pages.login_page import LoginPage
from common.logger import Logger


LOG = Logger()
def get_credential_list():
    path = os.path.join('common', 'static', 'default_credentials.json')
    with open(path, 'r') as dc_json:
        credentials_list = json.load(dc_json)
        updated_credentials = []
        for elm in credentials_list:
            if elm['username'] == 'locked_out_user':
                updated_credentials.append(pytest.param(
                    elm['username'],
                    elm['password'],
                    marks=pytest.mark.xfail(reason='User is not allowed to login')
                ))
            else:
                updated_credentials.append((elm['username'], elm['password']))
        return updated_credentials

@pytest.mark.parametrize('username,password', get_credential_list())
def test_login(driver, username, password):
    inventory_page = LoginPage(driver).login(username, password)
    inventory_page.assert_page_loaded()
    inventory_page.logout()
