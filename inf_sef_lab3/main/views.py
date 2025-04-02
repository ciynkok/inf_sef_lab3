from django.shortcuts import render, HttpResponse
from .models import Product
from .forms import ProductForm

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
