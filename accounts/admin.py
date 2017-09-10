from django.contrib import admin
from accounts import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email',
                                         'hometown', 'facebook_id', 'facebook_picture_url',
                                         )}),

        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(models.User, UserAdmin)

# Register your models here.
