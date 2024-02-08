from django.urls import path
from . import views

urlpatterns = [

 path('admin', views.admin_dashboard, name = 'admin'),
 path('admin_login', views.admin_login, name = 'admin_login'),
 path('admin_logout', views.admin_logout, name = 'admin_logout'),
 
 # product management
 path('manage_products/',views.manage_products,name="manage_products"),
 path('update/<str:id>',views.Update,name="update"),                                                                                                                      
 path('add_products', views.Add_products, name="add_products"),
 path('deleteproducts/<str:id>',views.Delete_products, name="deleteproducts"),

  # user management
 path('user_management', views.user_management, name = 'user_management'),
 path('block_user/<int:user_id>/', views.Block_user, name='block_user'),
 path('unblock_user/<int:user_id>/', views.Unblock_user, name='unblock_user'),
  
 # category managment
 path('manage_category/', views.manage_category, name='manage_category'),
 path('add_category', views.Add_category, name="add_category"),
 path('edit/<str:id>', views.Edit, name="edit"),
 path('delete/<str:id>', views.Delete, name='delete'),

 #order management
 path('orders', views.manage_orders, name = 'orders'),
 ]