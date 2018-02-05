from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.
    
    category_likes = Category.objects.order_by('-likes')[:5]
    page_views = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_likes,'pages': page_views}
    
    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_abt = {'author':'James Yao'}
    return render(request, 'rango/about.html', context = context_abt)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category = category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
        
    return render(request, 'rango/category.html', context_dict)

def show_page(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.filter(page = page)
        pages = Page.objects.get(slug=page_name_slug)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
        
    return render(request, 'rango/category.html', context_dict)
