from django.db import models
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Slide(models.Model):
    judul = models.CharField(max_length=200, blank=True, null=True)
    judul_samping = models.CharField(max_length=200, blank=True, null=True)
    gambar_slide = ResizedImageField(size=[1400, 600], quality=80, crop=['middle', 'center'] , upload_to='gambar/slide', blank=True, null=True, verbose_name="Gambar Slide (1400 x 600 pixel) *)")
    aktif = models.BooleanField(default=True)
   

    def __str__(self):
        return self.judul
    class Meta:
        verbose_name_plural ="Slide"


class Tahun(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=True)
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural ="Tahun"

class Produk(models.Model):
    nama_produk = models.CharField(max_length=200, blank=True, null=True, unique=True)
    gambar = ResizedImageField(size=[700, 400], quality=80, crop=['middle', 'center'] , upload_to='gambar/produk', blank=True, null=True, verbose_name="Gambar (700 x 400 pixel)*)")
    harga = models.PositiveIntegerField(blank=False, null=True)
    harga_pemasangan = models.PositiveIntegerField(blank=False, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    keterangan = RichTextField(blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.nama_produk)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.nama_produk
    class Meta:
        verbose_name_plural ="Produk"
    
class Pelanggan(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=False, null=True)
    wa = models.CharField(max_length=200, blank=False, null=True,verbose_name="No Whatsapp")
    alamat = RichTextField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=False, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural ="Pelanggan"

class DetailPasang(models.Model):
    STATUS=(
        ('Baru', 'Baru'),
        ('Proses' , 'Proses'),
        ('Selesai' , 'Selesai'),
    )
    KETERANGAN=(
        ('Belum Lunas', 'Belum Lunas'),
        ('Lunas' , 'Lunas'),
        ('Kadaluarsa' , 'Kadaluarsa'),
        ('Anda Batalkan' , 'Anda Batalkan'),
        ('Pembayaran Ditolak' , 'Pembayaran Ditolak'),
    )
    BANK=(
     
        ('bri' , 'bri'),
        ('bni' , 'bni'),
        ('bca' , 'bca'),
    )
    id_transaksi_va = models.CharField(max_length=200, blank=True, null=True)
    kode_pasang = models.CharField(max_length=200, blank=True, null=True)
    pelanggan = models.ForeignKey(Pelanggan, null=True, blank=True, on_delete=models.SET_NULL)
    produk = models.ForeignKey(Produk, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, blank=True, null=True, choices=STATUS)
    keterangan = models.CharField(max_length=200, blank=True, null=True, choices=KETERANGAN)
    bank = models.CharField(max_length=200, blank=True, null=True, choices=BANK)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    tanggal_pasang = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.pelanggan.nama
    class Meta:
        verbose_name_plural ="Detail Pasang"

class Perbaikan(models.Model):
    STATUS=(
        ('Baru', 'Baru'),
        ('Proses' , 'Proses'),
        ('Selesai' , 'Selesai'),
    )
    
    pelanggan = models.ForeignKey(Pelanggan, null=True, blank=True, on_delete=models.SET_NULL)
    detailpasang = models.ForeignKey(DetailPasang, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, blank=False, null=True, choices=STATUS)
    keluhan = RichTextField(blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.pelanggan.nama
    class Meta:
        verbose_name_plural ="Perbaikan"

class SettingPembayaran(models.Model):
    STATUS=(
        ('Baru', 'Baru'),
        ('Belum Lunas', 'Belum Lunas'),
        ('Lunas' , 'Lunas'),
        ('Kadaluarsa' , 'Kadaluarsa'),
        ('Anda Batalkan' , 'Anda Batalkan'),
        ('Pembayaran Ditolak' , 'Pembayaran Ditolak'),
    )
    id_transaksi_va = models.CharField(max_length=200, blank=True, null=True)
    tahun = models.CharField(max_length=200, blank=False, null=True)
    detailpasang = models.ForeignKey(DetailPasang, null=True, blank=True, on_delete=models.SET_NULL)
    bulan = models.CharField(max_length=200, blank=False, null=True)
    status = models.CharField(max_length=200, blank=False, null=True, choices=STATUS)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.bulan

    def __str__(self):
        if not self.detailpasang:
           return ""
        return str(f"{self.tahun} ({self.bulan})")
    class Meta:
        verbose_name_plural ="Setting Pembayaran"