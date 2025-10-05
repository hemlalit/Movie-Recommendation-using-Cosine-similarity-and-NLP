from django.shortcuts import render, redirect
from .models import Emenitites, Movie
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from .utils import df, recommend_movies

User = get_user_model()

@login_required(login_url="/login/")
def home(request):
    context = {
        'movie_list': df['movie_name'].values
    }
    return render(request, 'home.html', context)

@login_required(login_url="/login/")
def api_movies(request):
    movies_objs = Movie.objects.all()
    
    price = request.GET.get('price')
    if price:
        movies_objs = movies_objs.filter(price__lte=price)
        
    emenities = request.GET.get('emenities')
    if emenities:
        emenities = [int(e) for e in emenities.split(',') if e.isdigit()]
        movies_objs = movies_objs.filter(emenities__in=emenities).distinct()
    
    payload = [{'movie_name': movie_obj.movie_name,
                'movie_description': movie_obj.movie_description,
                'movie_image': movie_obj.movie_image,
                'price': movie_obj.price} for movie_obj in movies_objs]
    
    return JsonResponse(payload, safe=False)



def get_recommendations(request):
    if request.method == 'POST':
        movie_name = request.POST.get('movie_name')
        filter_by = request.POST.get('filter_by', 'overview')
        recommendations = recommend_movies(movie_name, filter_by)
        selected = df[df['movie_name'] == movie_name].iloc[0]
        return render(request, 'results.html', {
            'selected_movie': selected,
            'recommendations': recommendations,
            'filter_by': filter_by
        })

def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            
            user_obj = authenticate(username=username, password=password)
            
            if user_obj:
                login(request, user_obj)
                return redirect('/')
            
            messages.error(request, "Wrong Password")
            return redirect('/login/')
            
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
        
    return render(request, "login.html")

def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            
            messages.success(request, "Account created")
            return redirect('/login/')
        
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    
    return render(request, "register.html")

def custom_logout(request):
    logout(request)
    return redirect('login')