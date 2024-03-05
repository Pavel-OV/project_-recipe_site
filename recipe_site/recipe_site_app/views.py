from django.shortcuts import render

def index(request):
    return render(request, "recipe_site_app/index.html")