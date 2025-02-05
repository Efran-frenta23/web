from django.db import models

class Keranjang(models.Model):
    nama_barang = models.CharField(max_length=100)
    kuantitas = models.PositiveIntegerField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image= models.ImageField(upload_to="img/%y", blank=True)
    def save(self, *args, **kwargs):
        # Menghitung total harga
        self.total_harga = self.kuantitas * self.harga
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nama_barang} - {self.kuantitas} x {self.harga} = {self.total_harga}"

class image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption
    
class cartImage(models.Model):
    image = models.ImageField(upload_to='gambar')
