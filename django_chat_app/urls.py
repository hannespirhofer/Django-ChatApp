"""
URL configuration for django_chat_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from chat.views import index, login, register, logout, chat_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path(route="chat/", view=index, name="chat"),
    path(route="chat/<int:chatid>/", view=chat_detail, name="chat_detail"),
    path(route="login/", view=login, name="login"),
    path(route="logout/", view=logout, name="logout"),
    path(route="register/", view=register, name="register"),
    path(route="", view=index),
]

# This need to be set when inserting the debug toolbar as it uses the /__debug__/ path
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
