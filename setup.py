from setuptools import setup
from setuptools import setup, find_packages
setup(
    name = 'signalsfx',
    version = '0.1.0',
    packages = find_packages(),
     package_data={
        "": ["*.html", "*.css", "*.js"],
    },
    entry_points = {
        'console_scripts': [
            'signalsfx = signalsfx.__main__:main'
        ]
    },
    install_requires=["pywebview>=3.3.4"],
)