#!/usr/bin/env python
import argparse
import urllib.parse
from zapv2 import ZAPv2


class DastScan:
    def __init__(self, api_key):

        if api_key == '' or api_key == None:
            raise Exception('API key is required')

        self.context_id = 1
        self.context_name = 'Default Context'
        self.target_url = 'http://altoro.testfire.net'

        self.zap = ZAPv2(apikey=api_key)

        self.context_urls = {
            "exclude": [],
            "include": [
                'http://altoro.testfire.net*',
                'http://altoro.testfire.net/login.jsp',
                'http://altoro.testfire.net/doLogin*'
            ]
        }

    def set_context_urls(self):

        for url in self.context_urls.get("exclude"):
            print(f'excluding {url} from context')
            self.zap.context.exclude_from_context(self.context_name, url)

        for url in self.context_urls.get("include"):
            print(f'including {url} in context')
            self.zap.context.include_in_context(self.context_name, url)


    def set_logged_in_indicator(self):
        logged_in_regex = 'logout.jsp'
        self.zap.authentication.set_logged_in_indicator(self.context_id, logged_in_regex)
        print('Configured logged in indicator regex: ')


    def set_form_based_auth(self):
        login_url = 'http://altoro.testfire.net/doLogin'
        login_request_data = 'uid={%username%}&amp;passw={%password%}&amp;btnSubmit=Login'
        form_based_config = f'loginUrl={urllib.parse.quote(login_url)}&loginRequestData={urllib.parse.quote(login_request_data)}'
        self.zap.authentication.set_authentication_method(self.context_id, 'formBasedAuthentication', form_based_config)
        print('Configured form based authentication')


    def set_user_auth_config(self):
        user = 'Test User'
        username = 'admin'
        password = 'admin'

        user_id = self.zap.users.new_user(self.context_id, user)
        user_auth_config = f'uid={urllib.parse.quote(username)}&passw={urllib.parse.quote(password)}'
        self.zap.users.set_authentication_credentials(self.context_id, user_id, user_auth_config)
        self.zap.users.set_user_enabled(self.context_id, user_id, 'true')
        self.zap.forcedUser.set_forced_user(self.context_id, user_id)
        self.zap.forcedUser.set_forced_user_mode_enabled('true')
        print('User Auth Configured')
        return user_id


    def start_spider(self, user_id):
        self.zap.spider.scan_as_user(self.context_id, user_id, self.target_url, recurse='true')
        print('Started Scanning with Authentication')


    def run(self):
        self.set_context_urls()
        self.set_form_based_auth()
        self.set_logged_in_indicator()
        user_id = self.set_user_auth_config()
        self.start_spider(user_id)


if __name__ == "__main__":
    print('************ Running DastScan script')
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', dest='api_key', help='ZAP API key')
    args = parser.parse_args()

    dast_scan = DastScan(args.api_key)
    dast_scan.run()

