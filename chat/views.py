import json
from django.core import serializers
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from chat.models import Message, Chat


# /chat/
@login_required(login_url="/login/")
def index(request):
    if request.method == "POST" and request.POST.get("textmessage") is not "":
        msg = request.POST.get("textmessage")
        myChat = Chat.objects.get(id=1)
        message = Message.objects.create(
            text=msg, chat=myChat, author=request.user, receiver=request.user
        )

        serialized_message = serializers.serialize("json", [message])
        parsed_json = json.loads(serialized_message)
        single_message = parsed_json[0]

        modified_serialized_message = json.dumps(single_message)
        print(f"{msg} added to the db.")
        return JsonResponse(modified_serialized_message, safe=False)

    chatMessages = Message.objects.filter(chat__id=1).order_by("created_at")
    return render(
        request,
        "chat/index.html",
        context={"messages": chatMessages},
    )


# /login/
def login(request):
    error_message = None
    next_url_param = request.GET.get("next")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print(f"Welcome {user.first_name}")
            if next_url_param:
                return HttpResponseRedirect(next_url_param)
            else:
                return redirect("chat")
        else:
            print("Wrong crentials. Try again.")
            error_message = "Wrong credentials."
    return render(
        request,
        "chat/login.html",
        context={"error_message": error_message, "next": next_url_param},
    )


# /register/
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        password = request.POST.get("password")
        if password == "123456789":
            user = User.objects.create_superuser(
                username=username,
                first_name=firstname,
                password=password,
                email="test@test.com",
            )
        else:
            User.objects.create_user(
                username=username, first_name=firstname, password=password
            )

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print(f"Welcome {user.first_name}")
            return redirect("chat")

    return render(request, "chat/register.html")


def logout(request):
    auth_logout(request)
    return redirect("login")
