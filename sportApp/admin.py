from django.contrib import admin
from .models.user import User
from .models.account import Account

from django.contrib import admin
from .models.productos import productos


admin.site.register(User)
admin.site.register(Account)

admin.site.register(productos)