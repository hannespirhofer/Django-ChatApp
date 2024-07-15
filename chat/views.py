from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.method == "POST":
        msg = request.POST.get("textmessage")
        print(f"Received data from Input field: {msg} ")
        return redirect("chat")
    return render(
        request,
        "chat/index.html",
        context={"content": "Some random content directly from the render context!"},
    )
