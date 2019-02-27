from io import StringIO

import requests
from furl import furl


class AppsFlyer:
    DEFAULT_ENDPOINT = 'https://hq.appsflyer.com'
    RAW_DATA_REPORT_ADDITIONAL_FIELDS = ','.join([
        'install_app_store',
        'match_type',
        'contributor1_match_type',
        'contributor2_match_type',
        'contributor3_match_type',
        'device_category',
        'gp_referrer',
        'gp_click_time',
        'gp_install_begin',
    ])
    UNINSTALL_REPORT_ADDITIONAL_FIELDS = ','.join([
        'gp_referrer',
        'gp_click_time',
        'gp_install_begin',
    ])

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

        if 'additional_fields' in kwargs:
            args['additional_fields'] = kwargs.get('additional_fields')

        return args

    def __to_df(self, resp):
        import pandas as df

        if resp.status_code != requests.codes.ok:
            raise Exception(resp.text)

        return df.read_csv(StringIO(resp.text))

    def partners_report(self, date_from, date_to, as_df=False, **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        f.path = '/export/%s/partners_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)
        resp = requests.get(f.url)

        if as_df:
            return self.__to_df(resp)

        return resp

    def partners_by_date_report(self, date_from, date_to, as_df=False, **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        f.path = '/export/%s/partners_by_date_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)
        resp = requests.get(f.url)

        if as_df:
            return self.__to_df(resp)

        return resp

    def daily_report(self, date_from, date_to, as_df=False, **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        f.path = '/export/%s/daily_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)
        resp = requests.get(f.url)

        if as_df:
            return self.__to_df(resp)

        return resp

    def geo_by_date_report(self, date_from, date_to, as_df=False, **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        f.path = '/export/%s/geo_by_date_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)
        resp = requests.get(f.url)

        if as_df:
            return self.__to_df(resp)

        return resp

    def installs_report(self, date_from, date_to, as_df=False,
                        additional_fields=None,
                        **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        if additional_fields is None:
            kwargs['additional_fields'] = self.RAW_DATA_REPORT_ADDITIONAL_FIELDS
        f.path = '/export/%s/installs_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)
        resp = requests.get(f.url)

        if as_df:
            return self.__to_df(resp)

        return resp

    def in_app_events_report(self, date_from, date_to, as_df=False,
                             additional_fields=None,
                             **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        if additional_fields is None:
            kwargs['additional_fields'] = self.RAW_DATA_REPORT_ADDITIONAL_FIELDS
        f.path = '/export/%s/in_app_events_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)
        resp = requests.get(f.url)

        if as_df:
            return self.__to_df(resp)

        return resp

    def uninstall_events_report(self, date_from, date_to, as_df=False,
                                additional_fields=None,
                                **kwargs):
        f = furl(self.DEFAULT_ENDPOINT)
        if additional_fields is None:
            kwargs['additional_fields'] = self.UNINSTALL_REPORT_ADDITIONAL_FIELDS
        f.path = '/export/%s/uninstall_events_report/v5' % self.app_id
        f.args = self.__build_args(date_from, date_to, kwargs)
        resp = requests.get(f.url)

        if as_df:
            return self.__to_df(resp)

        return resp
