from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorator import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist


# GET data
@api_view(['GET'])
def all_todolist(request):
    # ດຶງຂໍ່ມູນຈາກ model Todolist "SELECT * from todolist"
    alltodolist = Todolist.objects.all()
    serializer = TodolistSerializer(alltodolist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


data = [
    {
        "title": "Phenomenal",
        "subtitle": "ເລີ່ມໃຫ້ບໍລິການແຕ່ ປີ 2018 ແມ່ນ Startup platfrom E-Commerce",
        "imageUrl": "https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Phenomenal.jpg",
        "detail": "ແມ່ນບໍລິສັດທີ່ດຳເນີນການດ້ານ platfrom E-Commerce ມີທັງ Application ແລະ Webapplication"
    },
    {
        "title": "Phenomenal Logistic",
        "subtitle": "ໃຫ້ບໍລິການຂົນສົ່ງລາວ - ຈີນ - ໄທ",
        "imageUrl": "https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/phenomenal_logistic2.jpg",
        "detail": "ເລີ່ມດຳເນີນການແມ່ນທ້າຍປີ 2021 ໃຫ້ບໍລິການຂົນສົ່ງລາວ - ຈີນ - ໄທ"
    },
    {
        "title": "Phenomenal Bottega",
        "subtitle": "ໃຫ້ບໍລິການຂາຍສິນຄ້າ ອອນໄລນ໌ ແບບ E-Commerce",
        "imageUrl": "https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Phenomenal%20Bottega.jpg",
        "detail": "ເລີ່ມດຳເນີນການແມ່ນປີ 2020 ຮັບສັ່ງຊື້ສິນຄ້າ ແລະ ເປັນການຂາຍສິນຄ້າ ອອນໄລນ໌ ແບບ E-Commerce"
    },
    {
        "title": "Phenomenal Book Cloud",
        "subtitle": "ໃຫ້ບໍລິການຂາຍໜັງສື ອອນໄລນ໌",
        "imageUrl": "https://raw.githubusercontent.com/Thitphavanh/Flutter-API/main/Phenomenal%20Bookcloud.jpg",
        "detail": "ເລີ່ມດຳເນີນການແມ່ນປີ 2021 ຂາຍໜັງສືທີ່ບໍ່ມີໜ້າຮ້ານ ເປັນການຂາຍແບບ ອອນໄລນ໌"
    }
]


def Home(request):
    return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})
