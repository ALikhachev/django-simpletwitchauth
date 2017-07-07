from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .fields import JSONField


@python_2_unicode_compatible
class TwitchAccount(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='twitch'
    )

    uid = models.CharField(verbose_name=_('uid'), max_length=139, unique=True)
    extra_data = JSONField(verbose_name=_('extra data'), default=dict)

    class Meta:
        verbose_name = _('twitch account')
        verbose_name_plural = _('twitch accounts')

    def __str__(self):
        return self.user.username

    def get_profile_url(self):
        return 'https://twitch.tv/' + self.account.extra_data.get('name')

    def get_avatar_url(self):
        return self.account.extra_data.get('logo')


@python_2_unicode_compatible
class OAuth2AccessToken(models.Model):
    account = models.OneToOneField(TwitchAccount)
    token = models.TextField(
        verbose_name=_('token'),
        help_text=_(
            'access token (OAuth2)'))
    token_secret = models.TextField(
        blank=True,
        verbose_name=_('token secret'),
        help_text=_(
            'refresh token (OAuth2)'))
    expires_at = models.DateTimeField(blank=True, null=True,
                                      verbose_name=_('expires at'))

    class Meta:
        verbose_name = _('oauth2 application token')
        verbose_name_plural = _('oauth2 application tokens')

    def __str__(self):
        return self.token
