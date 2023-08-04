from django.contrib import admin
from .models import User
from user_api.models import User


admin.site.register(User)


# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
