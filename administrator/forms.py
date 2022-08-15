from django import forms
from django.forms import ModelForm
from .models import Pelanggan, Slide, Perbaikan, DetailPasang, SettingPembayaran, Produk,Tahun
from django.contrib.auth.models import User

class TahunForm(ModelForm):
    class Meta:
        model = Tahun
        fields=['nama','aktif']
    labels = {
            'nama': 'Nama Tahun:',
        } 
class ProdukForm(ModelForm):
    class Meta:
        model = Produk
        fields=['nama_produk','gambar','harga','harga_pemasangan','keterangan']
    labels = {
            'nama_produk': 'Nama Produk:',
        } 
class SlideForm(ModelForm):
    class Meta:
        model = Slide
        fields=['judul','judul_samping','gambar_slide','aktif']

class PelangganForm(ModelForm):
    class Meta:
        model = Pelanggan
        fields=['nama','wa','alamat','email']
        widgets = {
            'wa': forms.TextInput(attrs={'class': 'form-control','placeholder':'628xxxxxxxxxx'}),

        }
class UserForm(ModelForm):
    class Meta:
        model= User
        fields =['username']
        help_texts ={
            'username':''
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','required':'required'}),
        }
        labels = {
            'username': 'Username*',
        }

class PerbaikanForm(ModelForm):
    class Meta:
        model = Perbaikan
        fields=['status']
        labels = {
                'status': 'Ubah Status:',
            }    
class DetailPasangForm(ModelForm):
    class Meta:
        model = DetailPasang
        fields=['status','tanggal_pasang']
        widgets = {
                'tanggal_pasang': forms.TextInput(attrs={'type':'date','class': 'form-control','required':'required'}),
            }
        labels = {
                'status': 'Ubah Status:',
            }    

class AjukanPerbaikanForm(ModelForm):
    class Meta:
        model = Perbaikan
        fields=['status']
        widgets = {
                'status': forms.Select(attrs={'type':'date','class': 'form-control','required':'required'}),
            }
        labels = {
                'status': 'Ubah Status:',
            } 