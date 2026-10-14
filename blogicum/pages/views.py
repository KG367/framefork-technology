"""D."""
from django.shortcuts import render


def about(request):
    """D."""
    return render(request, 'pages/about.html')


def rules(request):
    """D."""
    return render(request, 'pages/rules.html')
