# python-appsflyer

AppsFlyer API client library for Python.

## Installation

```bash
$ pip install git+https://github.com/ariarijp/python-appsflyer
```

## Usage

```python
from appsflyer import AppsFlyer

af = AppsFlyer(api_token='API_TOKEN',
               app_id='APP_ID')
resp = af.daily_report(date_from='2017-10-20',
                      date_to='2017-10-20',
                      timezone='Asia/Tokyo',
                      category='facebook')
print(resp.text)
```

## License

MIT

## Author

[ariarijp](https://github.com/ariarijp)
