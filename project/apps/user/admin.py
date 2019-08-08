from django.contrib import admin

from project.apps.user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('get_full_name',)

    def get_full_name(self, obj):
        return obj.get_full_name()

admin.site.register(User, UserAdmin)