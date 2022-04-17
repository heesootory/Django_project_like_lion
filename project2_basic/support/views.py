from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def faq(request):
    return HttpResponse("고객센터입니다.")



