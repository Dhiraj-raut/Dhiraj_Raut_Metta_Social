# currency/views.py

from django.shortcuts import render
from .models import Currency


def search_currency(request):
    if 'query' in request.GET:
        query = request.GET['query']
        currencies = Currency.objects.filter(name__icontains=query)
    else:
        currencies = Currency.objects.all()

    return render(request, 'currency/search_currency.html', {'currencies': currencies})


def currency_detail(request, currency_id):
    currency = Currency.objects.get(pk=currency_id)
    countries = currency.country_set.all()
    return render(request, 'currency/currency_detail.html', {'currency': currency, 'countries': countries})

