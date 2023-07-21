from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_param = request.GET.get('sort', 'name')
    template = 'catalog.html'
    sort_dict = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}
    phones = Phone.objects.all().order_by(sort_dict[sort_param])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    print(phone.name)
    return render(request, template, context)
