from django.urls import path
from .import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
     path('login', views.login_page, name='login_page'),
     path('logout', views.logoutPage, name='logout'),
     path('registrasi', views.registrasi, name='registrasi'),

     path('produk-wifi/<slug:slug>', views.detailproduk, name='detailproduk'),
     path('pasang-wifi/<slug:slug>', views.pasangproduk, name='pasangproduk'),
     path('simpanpasangbaru', views.simpanpasangbaru, name='simpanpasangbaru'),
     path('data-pasang/', views.datapasang, name='datapasang'),
     path('detailva/', views.detailva, name='detailva'),

     path('data-pasang-va/<kode_pemasangan>', views.datapasangva, name='datapasangva'),
      path('ajukan-perbaikan/', views.ajukanperbaikan, name='ajukanperbaikan'),
      path('ajukan-perbaikan/<kode_pemasangan>', views.ajukanperbaikanwifi, name='ajukanperbaikanwifi'),
      path('pembayaran-bulanan/', views.pembayaranbulanan, name='pembayaranbulanan'),

      path('data-bayar-va/<kode_pemasangan>', views.databayarva, name='databayarva'),
]
