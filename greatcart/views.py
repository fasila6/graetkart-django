from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products' : products, 
    }
    return render(request, 'home.html', context)


def admin_dashboard(request):
    return render(request, 'adminpannel/adminbase.html')



def products(request):
    return render(request, 'adminpannel/product.html')


def user_management(request):
    return render(request, 'adminpannel/user.html')


def category_management(request):
    return render(request, 'adminpannel/category.html')


def manage_orders(request):
    return render(request, 'adminpannel/orders.html')

        