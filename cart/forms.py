from django import forms
from .models import Keranjang

class KeranjangForm(forms.ModelForm):
    class Meta:
        model = Keranjang
        fields = ['nama_barang', 'kuantitas', 'harga', 'image']  
