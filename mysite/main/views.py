from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Product, Category, BlogPost, Tag
from .forms import StudentForm, AddressForm, ProductForm, BlogPostForm

# Student create (with address)
def student_create(request):
    if request.method == 'POST':
        s_form = StudentForm(request.POST)
        a_form = AddressForm(request.POST)
        if s_form.is_valid() and a_form.is_valid():
            student = s_form.save()
            address = a_form.save(commit=False)
            address.student = student
            address.save()
            return redirect('student_detail', pk=student.pk)
    else:
        s_form = StudentForm()
        a_form = AddressForm()
    return render(request, 'main/student_form.html', {'s_form': s_form, 'a_form': a_form})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'main/student_detail.html', {'student': student})

# Category and products
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'main/category_list.html', {'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'main/product_form.html', {'form': form})

# Blog posts and tags
def blog_list(request):
    posts = BlogPost.objects.all().prefetch_related('tags')
    return render(request, 'main/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'main/blog_detail.html', {'post': post})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            form.save_m2m()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'main/blog_form.html', {'form': form})
