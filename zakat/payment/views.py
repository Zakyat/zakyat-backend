from django.shortcuts import render, HttpResponse
from .payment import main

# Create your views here.

def test_view(request):
    main(request)
    return HttpResponse('DONE')
