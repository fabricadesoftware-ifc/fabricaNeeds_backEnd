from django.contrib import admin

from .models import Category, EventStatus

admin.site.register(Category)

admin.site.register(EventStatus)