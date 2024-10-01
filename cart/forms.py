from django import forms
from .models import Keranjang
from.models import image
class KeranjangForm(forms.ModelForm):
    class Meta:
        model = Keranjang
        fields = ['nama_barang', 'kuantitas', 'harga']
class ImageForm(forms.ModelForm):
    class Meta:
        model=image
        fields=("caption","image")