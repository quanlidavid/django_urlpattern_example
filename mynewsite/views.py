from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def homepage(request):
    return HttpResponse('Hello world!')


def manual(request, mode):
    return HttpResponse('Hello world! ' + mode)


def about(request):
    return HttpResponse('About!')


def listing(request, type='0'):
    return HttpResponse('Listing ' + type)


def post(request, yr, mon, day, post_num):
    return HttpResponse(
        yr + ' - ' + mon + ' - ' + day + ' - ' + post_num + '\n' + reverse('post-url', args=(yr, mon, day, post_num)))


def p1(request):
    return HttpResponse('P1')


def p2(request):
    return HttpResponse('P2')


def p3(request, v):
    return HttpResponse('P3' + ' - ' + v)
