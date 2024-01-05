#!/usr/bin/env python
import argparse
import urllib.parse
from zapv2 import ZAPv2


parser = argparse.ArgumentParser()
parser.add_argument('-k', dest='api_key', help='ZAP API key')
args = parser.parse_args()

context_id = 1
context_name = 'Default Context'
target_url = 'http://altoro.testfire.net'

zap = ZAPv2(apikey=args.api_key)

context_urls = {
    "exclude": [],
    "include": [
        'http://altoro.testfire.net*',
        'http://altoro.testfire.net/login.jsp',
        'http://altoro.testfire.net/doLogin*'
    ]
}

def set_context_urls():

    for url in context_urls.get("exclude"):
        print(f'excluding {url} from context')
        zap.context.exclude_from_context(context_name, url)

    for url in context_urls.get("include"):
        print(f'including {url} in context')
        zap.context.include_in_context(context_name, url)


def set_logged_in_indicator():
    logged_in_regex = 'logout.jsp'
    zap.authentication.set_logged_in_indicator(context_id, logged_in_regex)
    print('Configured logged in indicator regex: ')


def set_form_based_auth():
    login_url = 'http://altoro.testfire.net/doLogin'
    login_request_data = 'uid={%username%}&amp;passw={%password%}&amp;btnSubmit=Login'
    form_based_config = f'loginUrl={urllib.parse.quote(login_url)}&loginRequestData={urllib.parse.quote(login_request_data)}'
    zap.authentication.set_authentication_method(context_id, 'formBasedAuthentication', form_based_config)
    print('Configured form based authentication')


def set_user_auth_config():
    user = 'Test User'
    username = 'admin'
    password = 'admin'

    user_id = zap.users.new_user(context_id, user)
    user_auth_config = f'uid={urllib.parse.quote(username)}&passw={urllib.parse.quote(password)}'
    zap.users.set_authentication_credentials(context_id, user_id, user_auth_config)
    zap.users.set_user_enabled(context_id, user_id, 'true')
    zap.forcedUser.set_forced_user(context_id, user_id)
    zap.forcedUser.set_forced_user_mode_enabled('true')
    print('User Auth Configured')
    return user_id


def start_spider(user_id):
    zap.spider.scan_as_user(context_id, user_id, target_url, recurse='true')
    print('Started Scanning with Authentication')


set_context_urls()
set_form_based_auth()
set_logged_in_indicator()
user_id_response = set_user_auth_config()
start_spider(user_id_response)
