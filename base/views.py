from django.shortcuts import render
from .models import Movies
# Create your views here.
def home(request):
    title=request.GET.get('title')
    year=request.GET.get('year')
    director=request.GET.get('director')
    movies=""
    if year=="":
        if title=="":
            movies=Movies.objects.all().filter(director=director)
        elif director=="":
            movies=Movies.objects.all().filter(title=title)
        else:
            movies=Movies.objects.all().filter(title=title,director=director)
    elif director=="":
        movies=Movies.objects.all().filter(title=title,year=year)
    elif title=="":
        movies=Movies.objects.all().filter(director=director,year=year)
    
    return render(request, 'base/home.html',{'M':title,'Y':year,'D':director,'movies':movies})

def room(request):
    return render(request, 'base/room.html')