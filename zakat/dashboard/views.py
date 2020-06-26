from django.shortcuts import render


def gatherings(request):
    return render(request, 'gatherings.html', {})
