from django.contrib import admin
from .models import Settings


class SettingsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'create_at',
    ]


admin.site.register(Settings, SettingsAdmin)
