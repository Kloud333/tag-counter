#!/usr/bin/env python

from setuptools import setup

setup(
    name='tag-counter',
    version='1.0',
    description='Get HTML tags number by site url',
    author='Volodymyr Klekot',
    author_email='klekotVR@gmail.com',
    url='https://github.com/Kloud333/tag-counter',
    packages=['counter'],
    package_data={'': ['*.yaml']},
    install_requires=['requests', 'PyYAML', 'click', 'bs4', 'beautifulsoup4', 'logging'],
    license="MIT License",
    entry_points={
        'console_scripts':
            ['tagcounter = counter.counter:main']
        }
    )
