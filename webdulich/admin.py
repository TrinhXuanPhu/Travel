from django.contrib import admin
from .models import Post, FastNews, Experience , Discover, Food, Brand, Restaurant
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

admin.site.register(Post)
class PostForm(forms.Form):
    list_display = ('title', 'status')
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Post
        field = '__all__'
        
admin.site.register(FastNews)
class FastNews(forms.Form):
    list_display = ('title', 'status')
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = FastNews
        field = '__all__'
        
admin.site.register(Experience)
class Experience(forms.Form):
    list_display = ('title', 'status')
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Experience
        field = '__all__'
        
admin.site.register(Discover)
class Discover(forms.Form):
    list_display = ('title', 'status')
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Discover
        field = '__all__'
        
admin.site.register(Food)
class Food(forms.Form):
    list_display = ('title', 'status')
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Food
        field = '__all__'
        
admin.site.register(Brand)
class Brand(forms.Form):
    list_display = ('title', 'status')
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Brand
        field = '__all__'
        
admin.site.register(Restaurant)
class Restaurant(forms.Form):
    list_display = ('title', 'status')
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Restaurant
        field = '__all__'
        
      
