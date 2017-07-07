class AppSettings(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        from django.conf import settings
        getter = getattr(settings,
                         'TWITCH_AUTH_SETTING_GETTER',
                         lambda name, dflt: getattr(settings, name, dflt))
        return getter(self.prefix + name, dflt)

    @property
    def SCOPE(self):
        return self._setting("SCOPE", "user_read")

    @property
    def PROTOCOL(self):
        return self._setting("PROTOCOL", "http://")

    @property
    def CLIENT_ID(self):
        return self._setting("CLIENT_ID", "")

    @property
    def CLIENT_SECRET(self):
        return self._setting("CLIENT_SECRET", "")

    @property
    def REDIRECT_URI(self):
        return self._setting("REDIRECT_URI", "/")


# Ugly? Guido recommends this himself ...
# http://mail.python.org/pipermail/python-ideas/2012-May/014969.html
import sys

app_settings = AppSettings('TWITCH_AUTH_')
app_settings.__name__ = __name__
sys.modules[__name__] = app_settings
