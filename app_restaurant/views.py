from django.shortcuts import render

# Create your views here.
def home(request, template_name='restaurant_templates/index.html'):
    return render(request,template_name)