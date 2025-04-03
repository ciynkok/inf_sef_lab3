from django.shortcuts import render, HttpResponse
from .models import Product
from .forms import ProductForm, MyForm

# Create your views here.

def index(request):
    product = ''
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = get_product_by_name(form.cleaned_data.get('name'))
    else:
        form = ProductForm()

    context = {'form': form,
               'product': product}
    return render(request, 'main/index.html', context)

def get_product_by_name(name):
    return Product.objects.filter(name=name)


def csrf_view(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['myvalue']
            context = {'form': form, 'massage': value}
        else:
            context = {'form': form, 'massage': 'error'}
        return render(request, 'main/csrf_view.html', context=context)
    context = {'form': form, }
    return render(request, 'main/csrf_view.html', context=context)
