# from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return HttpResponse("Hello this is a test message for main page")