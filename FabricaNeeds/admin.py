from django.contrib import admin

from .models import Category, RecurrencyType

admin.site.register(Category)


admin.site.register(RecurrencyType)