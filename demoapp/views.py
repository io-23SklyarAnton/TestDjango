from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, i'm baby sklyar")


def second_page(request):
    return HttpResponse("<i>Thats the second page</i>")
