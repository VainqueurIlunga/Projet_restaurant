from django.shortcuts import render

# Create your views here.
def home(request, template_name='restaurant_templates/index.html'):
    return render(request,template_name)

def menu(request, template_name='restaurant_templates/menu.html'):
    return render(request,template_name)


def about(request, template_name='restaurant_templates/about.html'):
    return render(request,template_name)

def book(request, template_name='restaurant_templates/book.html'):
    return render(request,template_name)