"""View-функции приложения pages: статические страницы."""

from django.shortcuts import render


def about(request):
    """Статическая страница «О проекте»."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Статическая страница «Наши правила»."""
    template = 'pages/rules.html'
    return render(request, template)
