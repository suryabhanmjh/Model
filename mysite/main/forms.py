from django import forms
from .models import Student, Address, Product, BlogPost, Tag

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['line1','city','state','zipcode']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','title','description','price']

class BlogPostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    class Meta:
        model = BlogPost
        fields = ['title','body','tags']
