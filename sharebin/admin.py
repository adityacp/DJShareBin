# Django Imports
from django.contrib import admin

# Local Imports
from .models import Share


class ShareAdmin(admin.ModelAdmin):
    readonly_fields = ["created_on", "uid"]


admin.site.register(Share, ShareAdmin)
