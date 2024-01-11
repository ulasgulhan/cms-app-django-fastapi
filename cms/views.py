from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Product, SubCategory
from .forms import RegisterForm

# Create your views here.


def store(request, category_slug=None, subcategory_slug=None):
    if subcategory_slug != None:
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        products = Product.objects.filter(Q(category=subcategory), Q(status='Active') | Q(status='Modified')).order_by('-created_date')
        product_count = products.count()
        return render(request, 'store.html', {'products': products, 'product_count': product_count, 'subcategory': subcategory})
    elif category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        subcategories = category.subcategories.all()
        products = Product.objects.filter(Q(category__in=subcategories), Q(status='Active') | Q(status='Modified')).order_by('-created_date')
        product_count = products.count()
        return render(request, 'store.html', {'products': products, 'product_count': product_count, 'category': category})
    else:
        products = Product.objects.all().filter(Q(status='Active') | Q(status='Modified')).order_by('-created_date')
        product_count = products.count()
        return render(request, 'store.html', {'products': products, 'product_count': product_count})



def product_details(request, category_slug, subcategory_slug, product_slug):
    single_product = Product.objects.get(category__slug=subcategory_slug, slug=product_slug)
    context = {
        'single_product': single_product
    }
    return render(request, 'product_details.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
        else:
            return redirect('home')

    context = {
            'products': products,
            'product_count': product_count,
            'keyword': keyword,
        }
    return render(request, 'store.html', context)



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = RegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)




