from django.shortcuts import render
from django.http import JsonResponse

data = {'message': 'Hello World'}


def Home(request):
    return JsonResponse(data=data)
