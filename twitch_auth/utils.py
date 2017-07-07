from django.contrib.sites.models import Site
from django.utils.http import urlencode

from twitch_auth import app_settings


def get_absolute_uri(url):
    return app_settings.PROTOCOL + "%s%s" % (Site.objects.get_current().domain, url)


def build_url(url, extra_params):
    params = {
        'client_id': app_settings.CLIENT_ID,
        'scope': app_settings.SCOPE,
        'response_type': 'code'
    }
    params.update(extra_params)
    return "%s?%s" % (url, urlencode(params))
