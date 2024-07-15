from django.contrib import admin
from chat.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ("text", "created_at")
    list_filter = ("created_at",)
    search_fields = ["text"]


# Register your models here.
admin.site.register(Message, MessageAdmin)
