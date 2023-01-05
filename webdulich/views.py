from django.shortcuts import render
from .models import Post, FastNews, Experience, Discover, Food, Brand, Restaurant

def home_view(request):
    posts = Post.objects.all()
    fastnews = FastNews.objects.all()
    exps = Experience.objects.all()
    discovers = Discover.objects.all()
    foods = Food.objects.all()
    brands = Brand.objects.all()
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
        'fastnews': fastnews,
        'exps': exps,
        'discovers': discovers,
        'foods': foods,
        'brands': brands,
        'restaurants': restaurants,
        'nav': 'home'
    })
    
def exp_view(request):
    exps = Experience.objects.all()
    
    return render(request, 'exp.html',{
        'exps': exps,
        'nav': 'exp'
    })
    
def discover_view(request):
    discovers = Discover.objects.all()
    
    return render(request, 'discover.html',{
        'discovers': discovers,
        'nav': 'discover'
    })
    
def heritage_view(request):
    
    return render(request, 'heritage.html',{
        'nav': 'heritage'
    })
    
def fastnew_view(request):
    fastnews = FastNews.objects.all()
    
    
    return render(request, 'fastnew.html',{
        'fastnews': fastnews,
        'btn': 'fastnew'
    })
    
def food_view(request):
    foods = Food.objects.all()
    
    return render(request, 'food.html', {
        'foods': foods,
        'btn': 'food'
    })
    
def brand_view(request):
    brands = Brand.objects.all()
    restaurants = Restaurant.objects.all()
    
    return render(request, 'brand.html',{
        'restaurants': restaurants,
        'brands': brands,
        'btn': 'brand'
    })
    
def postDetail(request, id):
    pD = Post.objects.get(id =id)
    return render(request, 'postDetail.html', {'pD':pD})
    

    
    
