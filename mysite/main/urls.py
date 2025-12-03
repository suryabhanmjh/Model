from django.urls import path
from . import views

urlpatterns = [
    path('students/new/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),

    path('categories/', views.category_list, name='category_list'),
    path('products/new/', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/new/', views.blog_create, name='blog_create'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    # Preview the base template directly
    path('base/', views.base_view, name='base'),
]
