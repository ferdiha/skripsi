from django.urls import path
from . import views


urlpatterns = [
    path('', views.beranda_admin, name='beranda_admin'),

    path('tahun-admin/', views.tahun_admin, name='tahun_admin'),
    path('form-tahun/', views.formtahun_admin, name='formtahun_admin'),
    path('edit-tahun/<str:pk>', views.edittahun_admin, name='edittahun_admin'),
    path('delete-tahun/<str:pk>', views.deletetahun_admin, name='deletetahun_admin'),

    path('produk-admin/', views.produk_admin, name='produk_admin'),
    path('form-produk/', views.formproduk_admin, name='formproduk_admin'),
    path('edit-produk/<str:slug>', views.editproduk_admin, name='editproduk_admin'),
    path('delete-produk/<str:pk>', views.deleteproduk_admin, name='deleteproduk_admin'),

    path('slide-admin/', views.slide_admin, name='slide_admin'),
    path('form-slide/', views.formslide_admin, name='formslide_admin'),
    path('edit-slide/<str:pk>', views.editslide_admin, name='editslide_admin'),
    path('delete-slide/<str:pk>', views.deleteslide_admin, name='deleteslide_admin'),

     path('pelanggan-admin/', views.pelanggan_admin, name='pelanggan_admin'),
     path('form-pelanggan/', views.formpelanggan_admin, name='formpelanggan_admin'),
    path('edit-pelanggan/<str:pk>', views.editpelanggan_admin, name='editpelanggan_admin'),
    path('delete-pelanggan/<str:pk>', views.deletepelanggan_admin, name='deletepelanggan_admin'),


    path('perbaikan-admin/', views.perbaikan_admin, name='perbaikan_admin'),
    path('edit-perbaikan/<str:pk>', views.editperbaikan_admin, name='editperbaikan_admin'),

     path('setting-pembayaran/', views.settingpembayaran, name='settingpembayaran'),
      path('edit-pasang/<str:pk>', views.editpasang_admin, name='editpasang_admin'),
      path('delete-pasang/<str:pk>', views.deletepasang_admin, name='deletepasang_admin'),
  
     path('simpansettingpasang/', views.simpansettingpasang, name='simpansettingpasang'),

     path('belum-bayar-admin/', views.belumbayar_admin, name='belumbayar_admin'),
    path('delete-belum-bayar/<str:pk>', views.deletebelumbayar_admin, name='deletebelumbayar_admin'),
     path('bayar-admin/', views.bayar_admin, name='bayar_admin'),
    path('delete-bayar/<str:pk>', views.deletebayar_admin, name='deletebayar_admin'),
    

]
  
