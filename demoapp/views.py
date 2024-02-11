from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, i'm baby sklyar")


def showform(request):
    return render(request, "form.html")


def getform(request):
    name = request.POST["name"]
    id = request.POST["id"]
    return HttpResponse(f"Name is: {name}<br/>"
                        f"id is: {id}")


def handler404(request, exception):
    return HttpResponse('no page')
