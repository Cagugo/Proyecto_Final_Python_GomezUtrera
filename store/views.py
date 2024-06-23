
from .forms import ProductForm, AddToCartForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Cart
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

def home(request):
    return render(request, 'store/home.html')


def about(request):
    return render(request, 'store/about.html')

@login_required
def profile(request):
    return render(request, 'store/profile.html')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            if not created:
                cart_item.quantity += form.cleaned_data['quantity']
            else:
                cart_item.quantity = form.cleaned_data['quantity']
            cart_item.save()
            return redirect('cart')
    else:
        form = AddToCartForm()
    return render(request, 'store/add_to_cart.html', {'form': form, 'product': product})

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})