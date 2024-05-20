from django.shortcuts import render
from .models import Product, Purchase
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {
        'products': products
    })

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        Purchase.objects.create(user=request.user, product=product)
        return redirect('all_products') 
    return render(request, 'products/product_detail.html', {
        'product': product
        })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {
        'form': form
        })

@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update_product.html', {
        'form': form, 
        'product': product
        })

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('all_products')
    return render(request, 'products/delete_product.html', {'product': product})