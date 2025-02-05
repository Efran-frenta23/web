from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import Keranjang
from .forms import KeranjangForm
import datetime

def daftar_keranjang(request):
    keranjang = Keranjang.objects.all()
    return render(request, 'cart/daftar_keranjang.html', {'keranjang': keranjang})

def tambah_keranjang(request):
    if request.method == 'POST':
        form = KeranjangForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('daftar_keranjang')
    else:
        form = KeranjangForm()
    return render(request, 'cart/tambah_keranjang.html', {'form': form})

def edit_keranjang(request, pk):
    keranjang = get_object_or_404(Keranjang, pk=pk)
    if request.method == 'POST':
        form = KeranjangForm(request.POST, instance=keranjang)
        if form.is_valid():
            form.save()
            return redirect('daftar_keranjang')
    else:
        form = KeranjangForm(instance=keranjang)
    return render(request, 'cart/edit_keranjang.html', {'form': form})

def hapus_keranjang(request, pk):
    keranjang = get_object_or_404(Keranjang, pk=pk)
    if request.method == 'POST':
        keranjang.delete()
        return redirect('daftar_keranjang')
    return render(request, 'cart/hapus_keranjang.html', {'keranjang': keranjang})

def halaman_baru(request):

    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='jakarta'

    appid = 'c6c682d8bd98e843627ac386524e381a'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description= res['weather'][0]['description']
    icon= res['weather'][0]['icon']
    temp= res['main']['temp']
    day= datetime.date.today()
    
    return render(request, 'cart/halaman_baru.html', {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})

import requests
from django.shortcuts import render

def halaman_efan(request):
    movie_data = None 
    appid = '0c77e7a673d5b7da48634f333d594e17'  
    
    if request.method == 'POST' and 'movie' in request.POST:
        movie = request.POST['movie']
        url = f'https://api.themoviedb.org/3/search/movie?api_key={appid}&query={movie}'
        response = requests.get(url)
        
        if response.status_code == 200:
            movie_data = response.json() 

    return render(request, 'cart/halaman_efan.html', {'movie_data': movie_data})

from django.shortcuts import render
import requests

def movie_detail(request, movie_id):
    api_key = '0c77e7a673d5b7da48634f333d594e17'
    
    # Fetch movie details
    movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
    
    movie_response = requests.get(movie_url)
    credits_response = requests.get(credits_url)
    
    if movie_response.status_code == 200 and credits_response.status_code == 200:
        movie = movie_response.json()
        credits = credits_response.json()

        # Get the cast from the credits data
        cast = credits.get('cast', [])[:10]  # Limit to 10 main actors

        # Check if movie is part of a collection
        belongs_to_collection = movie.get('belongs_to_collection', None)

        return render(request, 'cart/movie_detail.html', {
            'movie': movie,
            'cast': cast,
            'belongs_to_collection': belongs_to_collection,
        })
    else:
        return render(request, 'cart/error.html', {'error': 'Movie not found'})
