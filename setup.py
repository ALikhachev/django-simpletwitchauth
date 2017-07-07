#!/usr/bin/env python
from setuptools import find_packages, setup

import twitch_auth

setup(
    name='django-simpletwitchauth',
    version=twitch_auth.__version__,
    description='Use this simple module to easily enable authorization in your Django application via Twitch API',
    long_description=open('README.rst').read(),
    url='https://github.com/ALikhachev/django-simpletwitchauth',
    author='Alexander Likhachev',
    author_email='likhachev96@gmail.com',
    install_requires=[
        'Django>=1.8',
        'requests'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='MIT License',
    keywords=['django auth authentication twitch external api'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)