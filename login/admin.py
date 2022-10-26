from django.contrib import admin

from login.views import login
from .models import login_1

admin.site.register(login_1)

# Register your models here.
