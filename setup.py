from setuptools import setup

setup(
    name = 'signalsfx',
    version = '0.1.0',
    packages = ['signalsfx'],
    entry_points = {
        'console_scripts': [
            'signalsfx = signalsfx.__main__:main'
        ]
    })