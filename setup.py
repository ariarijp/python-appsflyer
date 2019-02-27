from setuptools import setup

setup(
    name='python-appsflyer',
    version='0.2.1',
    description='AppsFlyer API client library for Python.',
    author='Takuya Arita',
    author_email='takuya.arita@gmail.com',
    url='https://github.com/ariarijp/python-appsflyer',
    packages=[
        'appsflyer',
    ],
    license='MIT',
    install_requires=[
        'requests',
        'furl',
    ],
)
