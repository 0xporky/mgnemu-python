# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='mgnemu',
    version='1.0.0',
    description='Software emulator of MG-N707TS cash machine',
    long_description='Software emulator of MG-N707TS cash machine',
    url='https://github.com/0xporky/mgnemu',
    author='Andrew Komar',
    author_email='0xporky@gmail.com',
    license='MIT',
    classifiers=[
        'Development status :: RElease',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='mgnemu MG-N707TS emulator',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'flask==0.12.2',
        'docopt==0.6.2',
        'flask_httpauth==3.2.3',
        'pymongo==3.6.0'
    ]
)
