from django.contrib import admin
from .models import Student, Address, Category, Product, Tag, BlogPost

class AddressInline(admin.StackedInline):
    model = Address
    can_delete = False
    fk_name = 'student'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    inlines = (AddressInline,)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','price','created')
    list_filter = ('category',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','published')
    filter_horizontal = ('tags',)
