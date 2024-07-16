from django.contrib import admin
from chat.models import Message, Chat


class MessageAdmin(admin.ModelAdmin):
    fields = ["text", "chat", "created_at", "author", "receiver"]
    list_display = ("text", "chat", "created_at", "author", "receiver")
    list_filter = ("created_at",)
    search_fields = ["text"]


# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
