from django.shortcuts import render, redirect
from .models import *
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()

            Log.objects.create(
                log_type='CREATE',
                product=product,
                message=f'New product created: {product.name} (ID: {(product.id)})'
            )
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    old_name = product.name
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            Log.objects.create(
                log_type='UPDATE',
                product=product,
                message=f'Updated product {pk}: old name={old_name}, new name={product.name}'
            )
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    Log.objects.create(
        log_type='DELETE',
        product=product,
        message=f'Deleted product {pk}: {product.name}')
    product.delete()
    return redirect('product_list')