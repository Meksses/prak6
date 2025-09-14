from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import OrderForm

def home(request):
    return render(request, 'store/home.html')

def products_list(request):
    products = Product.objects.all()
    return render(request, 'store/products_list.html', {'products': products})

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'store/categories_list.html', {'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'store/category_detail.html', {'category': category})

def cart(request):
    return render(request, 'store/cart.html')

def order_create(request, product_id):
    from .models import Product
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'store/order_form.html', {'form': form, 'product': product})

def order_success(request):
    return render(request, 'store/order_success.html')
