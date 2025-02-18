from django.urls import path
from . import views
from .views import halaman_baru
from .views import halaman_efan
from .views import movie_detail

urlpatterns = [
    path('', views.daftar_keranjang, name='daftar_keranjang'),
    path('tambah/', views.tambah_keranjang, name='tambah_keranjang'),
    path('tambah_sql/', views.tambah_keranjang_sql, name='tambah_keranjang_sql'),
    path('edit/<int:pk>/', views.edit_keranjang, name='edit_keranjang'),
    path('hapus/<int:pk>/', views.hapus_keranjang, name='hapus_keranjang'),
    path('halaman_baru/', views.halaman_baru, name='halaman_baru'),
    path('halaman_efan/', views.halaman_efan, name='halaman_efan'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]