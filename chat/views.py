from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
    # This refers to the templates/shared from the main app
    # return render(
    #     request, "shared/shared.html"
    # )

    # for debug_toolbar
    # print("From View: Request User:", request.user)
    # print("From View: Request Method:", request.method)
    # print("From View: Request Path:", request.path)

    # CAUTION for testing purpose only as this reveals sensitive data
    # for attr in dir(request):
    #     if not attr.startswith("_"):
    #         try:
    #             print(f"{attr}: {getattr(request, attr)}")
    #         except Exception as e:
    #             print(f"An error occurred.\n{e}")

    # this refers to the templatesx within the app itself
    return render(
        request,
        "chat/index.html",
        context={"content": "Some random content directly from the render context!"},
    )
