from django.db import models
from django.urls import reverse

# ONE-TO-ONE: Student <-> Address
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Address(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='address')
    line1   = models.CharField(max_length=255)
    city    = models.CharField(max_length=100)
    state   = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.line1}, {self.city}"

# ONE-TO-MANY: Category -> Product (or Article)
class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title    = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price    = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

# MANY-TO-MANY: BlogPost <-> Tag
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title   = models.CharField(max_length=250)
    body    = models.TextField()
    tags    = models.ManyToManyField(Tag, related_name='posts', blank=True)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
