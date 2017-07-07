Simple Twitch auth
==================

| Wanna enable your awesome Django application to register and
  authenticate user using Twitch profiles?
| This application was created especially for your needs

Features
--------

-  Easy to use
-  Ready to Twitch channel name changes
-  Username cases are synchronized to Twitch display\_name
-  User emails are synchronized to Twitch

Installation
------------

Ensure that `Django ‘sites’ framework`_ is enabled.

Python package:
~~~~~~~~~~~~~~~

::

    pip install django-simpletwitchauth

settings.py:
~~~~~~~~~~~~

Add ``twitch_auth`` to INSTALLED\_APPS

Add ``twitch_auth.backends.OAuth2Backend`` to AUTHENTICATION\_BACKENDS

Set `Twitch application`_ settings

Example using django-environ:

::

    env = environ.Env()

    TWITCH_AUTH_CLIENT_ID = env('TWITCH_CLIENT_ID', default='some_client_id')
    TWITCH_AUTH_CLIENT_SECRET = env('TWITCH_CLIENT_SECRET', default='some_client_secret')

All available settings:
^^^^^^^^^^^^^^^^^^^^^^^

TWITCH\_AUTH\_SCOPE
'''''''''''''''''''

Defines OAuth2 token scope

Defaults to ``user_read``

TWITCH\_AUTH\_PROTOCOL
''''''''''''''''''''''

Defines protocol that is used to build full authentication callback URI

Defaults to ``http://``

TWITCH\_AUTH\_CLIENT\_ID
''''''''''''''''''''''''

Defines Twitch application client ID

TWITCH\_AUTH\_CLIENT\_SECRET
''''''''''''''''''''''''''''

Defines Twitch application client secret

TWITCH\_AUTH\_REDIRECT\_URI
'''''''''''''''''''''''''''

Defines default redirect URI after successful authentication

Defaults to ``/``

Usage
-----

-  Run migrations to create database tables for entities.
-  Add somewhere in your templates link to url ``login_twitch``

.. _Django ‘sites’ framework: https://docs.djangoproject.com/en/1.11/ref/contrib/sites/
.. _Twitch application: https://www.twitch.tv/settings/connections