# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='mgnemu',
    version='0.1.0',
    description='Software emulator of MG-N707TS cash machine',
    long_description='Software emulator of MG-N707TS cash machine',
    url='https://github.com/0xporky/mgnemu',
    author='Andrew Komar',
    author_email='0xporky@gmail.com',
    license='MIT',
    classifiers=[
        'Development status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='mgnemu MG-N707TS emulator',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'Flask'
    ]
)
