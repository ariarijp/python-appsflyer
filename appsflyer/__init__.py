import requests
from furl import furl


class AppsFlyer:
    DEFAULT_ENDPOINT = 'https://hq.appsflyer.com'

    def __init__(self, api_token, app_id):
        self.api_token = api_token
        self.app_id = app_id

    def __build_args(self, date_from, date_to, kwargs):
        args = {
            'api_token': self.api_token,
            'from': date_from,
            'to': date_to,
            'timezone': kwargs.get('timezone', 'UTC'),
            'currency': kwargs.get('currency', 'preferred'),
        }

        if 'media_source' in kwargs:
            args['media_source'] = kwargs.get('media_source')

        if 'event_name' in kwargs:
            args['event_name'] = kwargs.get('event_name')

        if 'category' in kwargs:
            args['category'] = kwargs.get('category')

        return args

    def partners_report(self, date_from, date_to, **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        f.path = '/export/%s/partners_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)

        return requests.get(f.url)

    def partners_by_date_report(self, date_from, date_to, **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        f.path = '/export/%s/partners_by_date_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)

        return requests.get(f.url)

    def daily_report(self, date_from, date_to, **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        f.path = '/export/%s/daily_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)

        return requests.get(f.url)

    def geo_by_date_report(self, date_from, date_to, **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        f.path = '/export/%s/geo_by_date_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)

        return requests.get(f.url)
