from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
from django.contrib import messages,auth
from accounts.models import Account

# Create your views here.



#cosumize admin pannel

def admin_dashboard(request):
    return render(request, 'adminpannel/adminbase.html')


def admin_login(request):
    if request.user.is_authenticated and request.user.is_admin:
        return redirect('admin')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None and user.is_admin and user.is_active:
            login(request, user)
            return redirect('admin')
        else:
            messages.error(request, "Invalid credentiols,")
            return redirect('admin_login')

    return render(request, 'adminpannel/admin_login.html')


def admin_logout(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('admin_login') 


    


#  product management

def manage_products(request):
    products = Product.objects.all()
    context = {
        'products' : products,
        }
    
    return render(request,'adminpannel/manage_products.html', context)


def Add_products(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        images = request.FILES.get('images')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        is_available = request.POST.get('is_available')
        category = request.POST.get('category')  

        category = get_object_or_404(Category, category_name=category)

        if Product.objects.filter(product_name=product_name).exists():
            messages.error(request, 'A product with the same name already exists.')
            return redirect('manage_products')
        else:
            products = Product(
                product_name=product_name,
                slug = slug,
                description=description,
                images=images,
                price=price,
                stock=stock,
                is_available=is_available,
                category=category,  
            )
            products.save()
            return redirect('manage_products')
        

    return render(request, "adminpannel/manage_products.html")




def Update(request, id):
    products = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product_name = request.POST.get('product_name')
        slug = request.POST.get('slug')
        price = request.POST.get('price')
        images = request.FILES.get('images')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        created_date = request.POST.get('created_date')
        modified_date = request.POST.get('modified_date')
         

        products.product_name = product_name
        products.slug = slug
        products.price = price
        products.images = images
        products.description = description
        products.stock = stock
        products.created_date = created_date
        products.modified_date = modified_date 
        products.save()

        return redirect('manage_products')

    return render(request, 'adminpannel/manage_products.html', {'products': products})
    

def Delete_products(request, id):
    products = get_object_or_404(Product, id=id)

    if request.method == "POST":
        products.delete()
        return redirect('manage_products')

    return render(request, 'adminpannel/manage_products.html', {'products': products})





# User management

def user_management(request):
    user = Account.objects.all()
    context = {
        'user' : user,
        }

    return render(request, 'adminpannel/user.html', context)



def Block_user(request, user_id):
    try:
        user = get_object_or_404(Account, id=user_id)
        if not user.is_blocked:
            user.is_blocked = True
            user.save()
            messages.success(request, "This User has been blocked.")
            return redirect('user_management')
        else:
            messages.warning(request, "This User is already blocked")
            return redirect('user_management')
    except Account.DoesNotExist:
        messages.error(request, "User not found")

    return redirect('user_management') 
        
    
def Unblock_user(request, user_id):
    try:
        user = get_object_or_404(Account, id=user_id)
        if user.is_blocked:
            user.is_blocked = False
            user.save()
            messages.success(request, " This User has been unblocked.")
            return redirect('user_management')
        else:
            messages.warning(request, "This User is not unblocked")
            return redirect('user_management')
    except Account.DoesNotExist:
        messages.error(request, "User not found")
       
    return render(request,'adminpannel/user_management.html') 

    
    

# category management


def manage_category(request):
    category = Category.objects.all()
    context = {
        'category' : category,
        }
    return render(request, 'adminpannel/manage_category.html', context)


def Add_category(request):
    if request.method == 'POST':
        cat_image = request.FILES.get('cat_image')
        category_name = request.POST.get('category_name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')


        category= Category(
            category_name = category_name,
            slug = slug,
            description= description,
            cat_image = cat_image
        )
        
        category.save()

        return redirect('manage_category') 

    return render(request, 'adminpannel/manage_category.html', {'category': category})



def Edit(request,id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')
        cat_image = request.FILES.get('cat_image')
        
        category.category_name = category_name
        category.description = description
        category.cat_image = cat_image  
        category.save()

        return redirect('manage_category')

    return render(request, 'adminpannel/manage_category.html', {'category': category})


def Delete(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        category.delete()
        return redirect('manage_category')

    return render(request, 'adminpannel/manage_category.html', {'category': category})


def manage_orders(request):
    return render(request, 'adminpannel/orders.html')



