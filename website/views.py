from django.shortcuts import render, get_object_or_404, redirect
from administrator.models import Pelanggan, Slide, Perbaikan, DetailPasang, SettingPembayaran, Produk,Tahun
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini, ijinkan_pengguna
import urllib.request
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import uuid
import midtransclient
from administrator.forms import AjukanPerbaikanForm, UserForm, PelangganForm
from django.http import Http404
from .constants import PAYMENT_STATUS
MIDTRANS_CORE = midtransclient.CoreApi(
    is_production=not settings.DEBUG,
    server_key='SB-Mid-server-lYFlujbf6kblULZvgL5BzyAM',
    client_key='SB-Mid-client-Mwrb_UsPSl3P4h3x',
)

def produkFooter(request):
    produkfooter = Produk.objects.all().order_by('-id')[:5]
    return {'produkfooter':produkfooter}

def beranda (request):
    slideatas = Slide.objects.filter(aktif = True).order_by('-id')[:1]
    slide = Slide.objects.filter(aktif = True).order_by('-id')[1:6]
    produk = Produk.objects.order_by('-id')
    

    context = {
        'judul': 'Halaman Utama Wifi Qiana',
        'menu': 'beranda',
        'slideatas':slideatas,
        'slide':slide,
        'produk':produk,
       
    }
    return render(request, 'beranda.html', context)

def detailproduk (request, slug):
    produk = get_object_or_404(Produk, slug=slug)
    context = {
        'judul': 'Halaman Detail Produk Wifi Qiana',
        'menu': 'beranda',
        'produkdetail':produk,
    }
    return render(request, 'detailproduk.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])     
def pasangproduk (request, slug):
    produk = get_object_or_404(Produk, slug=slug)
    context = {
        'judul': 'Halaman Detail Produk Wifi Qiana',
        'menu': 'beranda',
        'produkdetail':produk,
    }
    return render(request, 'pasangproduk.html', context)
@tolakhalaman_ini
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cocokan = authenticate(request, username=username, password=password)
        if cocokan is None:
            messages.error(request, 'Usernama dan Password salah')
            return redirect('login_page')
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        # print(result['success'])
        if result['success']== False:
            messages.error(request, 'CaptCaha Masih Belum dicentang')
            return redirect('login_page')
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda_admin')
    context = {
        'judul': 'Halaman Login',
        'menu': 'login',
    }
    return render(request, 'login.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])  
def simpanpasangbaru(request):
    if request.method == "POST":
        idproduk = request.POST.get('id_produk')
        bank = request.POST.get('bank')
        id_produk = Produk.objects.get(id=idproduk)
        idpelanggan = request.user.pelanggan.id
        id_pelanggan = Pelanggan.objects.get(id=idpelanggan)

        kode_pasang = datetime.datetime.now().strftime("%Y%m%d%H%M%S")


        form =DetailPasang.objects.create(pelanggan=id_pelanggan,produk=id_produk)
        form.status = 'Baru'
        form.bank = bank
        form.kode_pasang = kode_pasang
        form.save()
        
        return JsonResponse({'status': 'Save' })
    else:
        return JsonResponse({'status' : 0})


@tolakhalaman_ini   
def registrasi(request):
    form = PelangganForm()
    formuser = UserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.is_active = True
        user.save()

        akses = Group.objects.get(name='pelanggan')
        user.groups.add(akses)

        formsimpan = PelangganForm(request.POST)
        if formsimpan.is_valid():
            data = formsimpan.save()
            data.user = user
            data.save()
            return redirect('login_page')
  
    context = {
        'judul': 'Halaman Registrasi',
        'menu': 'registrasi',
        'form':form,
        'formuser':formuser
    }
    return render(request, 'registrasi.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login_page')


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])     
def datapasang (request):
    
    context = {
        'judul': 'Halaman Pasang Wifi Qiana',
        'menu': 'pasangbaru',
    
    }
    return render(request, 'datapasang.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])     
def detailva (request):
    idpelanggan = request.user.pelanggan.id
    pelanggan = Pelanggan.objects.get(id=idpelanggan)
    pasang = DetailPasang.objects.filter(pelanggan__id=pelanggan.id).order_by('-id')
    context = {
        'pasang':pasang,
    }
    return render(request, 'detailva.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])     
def datapasangva (request, kode_pemasangan):
    idpelanggan = request.user.pelanggan.id
    pelanggan = Pelanggan.objects.get(id=idpelanggan)
    pasang = DetailPasang.objects.get(pelanggan__id=pelanggan.id, kode_pasang=kode_pemasangan)
   
    if pasang.id_transaksi_va:
        resp = MIDTRANS_CORE.transactions.status(pasang.id_transaksi_va)
        pasang.keterangan = PAYMENT_STATUS[resp.get('transaction_status')]
        pasang.save()
    else:
        resp = MIDTRANS_CORE.charge({
            "payment_type": "bank_transfer",
            "transaction_details": {
                "order_id": uuid.uuid4().hex,  # mocked order id
                "gross_amount": pasang.produk.harga_pemasangan
            },
            "bank_transfer": {
                "bank": pasang.bank
            },
            'metadata': {
                'product_id': pasang.produk.id
            },
        })
     
        pasang.id_transaksi_va = resp.get('transaction_id')
        pasang.keterangan = PAYMENT_STATUS[resp.get('transaction_status')]
        pasang.save()  
    
    context = {
        'pasang':pasang,
        'midtrans_status': resp.get('transaction_status'),
        'virtual_accounts': resp.get('va_numbers'),
    }
    return render(request, 'datapasangva.html', context)




@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])     
def ajukanperbaikan (request):
    idpelanggan = request.user.pelanggan.id
    pelanggan = Pelanggan.objects.get(id=idpelanggan)
    perbaikan = DetailPasang.objects.filter(pelanggan__id=pelanggan.id, status="Selesai")
    data = Perbaikan.objects.filter(pelanggan__id=pelanggan.id)
    context = {
        'judul': 'Halaman Ajukan Perbaikan Wifi Qiana',
        'menu': 'ajukanperbaikan',
        'perbaikan':perbaikan,
        'data':data
    }
    return render(request, 'ajukanperbaikan.html', context)
@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])     
def ajukanperbaikanwifi(request, kode_pemasangan):
    
    pasang = get_object_or_404(DetailPasang, kode_pasang=kode_pemasangan)
    idpasang = DetailPasang.objects.get(id=pasang.id)
    idpelanggan = request.user.pelanggan.id
    pelanggan = Pelanggan.objects.get(id=idpelanggan)
    if request.method == 'POST':
        keluhan = request.POST.get('keluhan')
        simpan = Perbaikan(pelanggan = pelanggan, detailpasang=idpasang, keluhan = keluhan, status="Baru")
        simpan.save() 
        return redirect('ajukanperbaikan')
    
    context = {
        'judul': 'Halaman Form Ajukan Perbaikan Wifi Qiana',
        'menu': 'ajukanperbaikan',
        'pasang':pasang,
        
    
    }
    return render(request, 'formajukanperbaikan.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])     
def pembayaranbulanan (request):
    idpelanggan = request.user.pelanggan.id
    pelanggan = Pelanggan.objects.get(id=idpelanggan)
    data = SettingPembayaran.objects.filter(detailpasang__pelanggan__id=pelanggan.id)
    context = {
        'judul': 'Halaman Pembayaran Wifi Qiana',
        'menu': 'pembayaranwifi',
        'data':data
    }
    return render(request, 'pembayaranbulanan.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['pelanggan'])     
def databayarva (request, kode_pemasangan):
    idpelanggan = request.user.pelanggan.id
    pelanggan = Pelanggan.objects.get(id=idpelanggan)
    bayar = SettingPembayaran.objects.get(detailpasang__pelanggan__id=pelanggan.id, detailpasang__kode_pasang=kode_pemasangan)
   
    if bayar.id_transaksi_va:
        resp = MIDTRANS_CORE.transactions.status(bayar.id_transaksi_va)
        bayar.status = PAYMENT_STATUS[resp.get('transaction_status')]
        bayar.save()
    else:
        resp = MIDTRANS_CORE.charge({
            "payment_type": "bank_transfer",
            "transaction_details": {
                "order_id": uuid.uuid4().hex,  # mocked order id
                "gross_amount": bayar.detailpasang.produk.harga
            },
            "bank_transfer": {
                "bank": bayar.detailpasang.bank
            },
            'metadata': {
                'product_id': bayar.detailpasang.produk.id
            },
        })
     
        bayar.id_transaksi_va = resp.get('transaction_id')
        bayar.status = PAYMENT_STATUS[resp.get('transaction_status')]
        bayar.save()  
    
    context = {
        'bayar':bayar,
        'midtrans_status': resp.get('transaction_status'),
        'virtual_accounts': resp.get('va_numbers'),
    }
    return render(request, 'databayarva.html', context)