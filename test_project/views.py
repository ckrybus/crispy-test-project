from django.shortcuts import render


def index(request):
    return render(request, "test_project/index.html", {})
