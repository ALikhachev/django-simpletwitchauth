from django.contrib import admin

from .models import TwitchAccount, OAuth2AccessToken


class TwitchAccountAdmin(admin.ModelAdmin):
    search_fields = ['user']
    raw_id_fields = ('user',)
    list_display = ('user', 'uid')


class OAuth2AccessTokenAdmin(admin.ModelAdmin):
    raw_id_fields = ('account',)
    list_display = ('account', 'truncated_token', 'expires_at')
    list_filter = ('expires_at',)

    def truncated_token(self, token):
        max_chars = 40
        ret = token.token
        if len(ret) > max_chars:
            ret = ret[0:max_chars] + '...(truncated)'
        return ret

    truncated_token.short_description = 'Token'


admin.site.register(TwitchAccount, TwitchAccountAdmin)
admin.site.register(OAuth2AccessToken, OAuth2AccessTokenAdmin)
