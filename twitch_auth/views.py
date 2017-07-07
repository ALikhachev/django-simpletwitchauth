import logging
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from twitch_auth import app_settings
from twitch_auth.utils import build_url

logger = logging.getLogger(__name__)


def login(request):
    redirect_to = request.GET.get('next', app_settings.REDIRECT_URI)
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    authorize_url = 'https://api.twitch.tv/kraken/oauth2/authorize'
    params = {
        'redirect_uri': request.build_absolute_uri(reverse('callback_twitch')),
    }
    verifier = get_random_string()
    request.session['state'] = (redirect_to, verifier)
    params['state'] = verifier
    return HttpResponseRedirect(build_url(authorize_url, params))


def get_next_uri(request, verifier_ext):
    state, verifier = request.session.pop('state')
    if verifier != verifier_ext:
        raise PermissionDenied()
    return state


def callback(request):
    if 'error' in request.GET:
        error_message = _('You denied access to your Twitch account') \
            if request.GET['error'] == 'access_denied' else _('Error while authentication via Twitch API')
        messages.error(request, error_message)
        logger.error('[Twitch Auth] %s: %s' % (request.META['REMOTE_ADDR'], request.GET['error_description']))
        return HttpResponseRedirect('/')
    redirect_to = get_next_uri(request, request.GET['state'])
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    user = authenticate(code=request.GET['code'])
    if user and user.is_active:
        auth_login(request, user)
        messages.success(request, _('You successfully logged in'))
        return HttpResponseRedirect(redirect_to)
    else:
        messages.error(request, _('Cannot authenticate you'))
        return HttpResponseRedirect('/')


@csrf_protect
def logout(request):
    auth_logout(request)
    messages.success(request, _('You successfully logged out'))
    return HttpResponseRedirect('/')
