from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelanggan, Slide, Perbaikan, DetailPasang, SettingPembayaran, Produk,Tahun
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from datetime import datetime, timedelta, time
today = datetime.now().date()
from .forms import DetailPasangForm, TahunForm, ProdukForm, SlideForm, PelangganForm,UserForm,PerbaikanForm
from django.contrib.auth.decorators import login_required
from website.decorators import ijinkan_pengguna,pilihan_login
from django.http import JsonResponse

@login_required(login_url='login_page')
@pilihan_login
def beranda_admin (request):
    jmlproduk = Produk.objects.all().count()
    jmlpelanggan = Pelanggan.objects.all().count()
    jmlperbaikan = Perbaikan.objects.all().count()
    jmlslide = Slide.objects.all().count()
    jmltahun = Tahun.objects.all().count()
    jmlbelumbayar = SettingPembayaran.objects.filter(date_created=today).count()
    context = {
        'judul': 'Halaman Beranda',
        'menu': 'beranda',
        'jmlproduk':jmlproduk,
        'jmlpelanggan':jmlpelanggan,
        'jmlslide':jmlslide,
        'jmltahun':jmltahun,
        'jmlbelumbayar':jmlbelumbayar,
        'jmlperbaikan':jmlperbaikan


    }
    return render(request, 'admin_beranda.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def tahun_admin(request):
    tahun = Tahun.objects.all()
    
    context = {
        'data': tahun,
        'judul': 'Halaman Tahun',
        'menu': 'setting',
    }
    return render(request, 'admin_tahun.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formtahun_admin(request):
    form = TahunForm()
    if request.method == 'POST':
        formsimpan = TahunForm(request.POST)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('tahun_admin')
    context = {
       'judul': 'Halaman Form Tahun',
        'menu': 'setting',
        'form':form
    }
    return render(request, 'admin_formtahun.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def edittahun_admin(request, pk):
    tahun = Tahun.objects.get(id=pk)
    form = TahunForm(instance=tahun)
    if request.method == 'POST':
        formsimpan = TahunForm(request.POST, instance=tahun)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('tahun_admin')
    context = {
       'judul': 'Halaman Edit Tahun',
        'menu': 'setting',
        'form':form
    }
    return render(request, 'admin_formtahun.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletetahun_admin(request, pk):
    hapus = Tahun.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('tahun_admin')

    context = {
        'judul': 'Halaman Hapus Tahun',
        'menu': 'setting',
        'hapus':hapus  
    }
    return render(request, 'admin_hapustahun.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def produk_admin(request):
    produk = Produk.objects.all()
    context = {
        'data': produk,
        'judul': 'Halaman Produk Wifi',
        'menu': 'produk',
    }
    return render(request, 'admin_produk.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator'])   
def formproduk_admin(request):
    form = ProdukForm()
    if request.method == 'POST':
        formsimpan = ProdukForm(request.POST,request.FILES)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('produk_admin')
    context = {
        'judul': 'Halaman Form Produk Wifi',
        'menu': 'produk',
        'form':form
    }
    return render(request, 'admin_formproduk.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editproduk_admin(request, slug):
    produk = Produk.objects.get(slug=slug)
    form = ProdukForm(instance=produk)
    if request.method == 'POST':
        formsimpan = ProdukForm(request.POST,request.FILES, instance=produk)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('produk_admin')
    context = {
        'judul': 'Halaman Edit Produk Wifi',
        'menu': 'produk',
        'form':form
    }
    return render(request, 'admin_formproduk.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deleteproduk_admin(request, pk):
    hapus = Produk.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('produk_admin')
    context = {
        'judul': 'Halaman Hapus Produk Wifi',
        'menu': 'produk',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusproduk.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def slide_admin(request):
    slide = Slide.objects.all()
    context = {
        'data': slide,
       'judul': 'Halaman Slide',
        'menu': 'slide',
    }
    return render(request, 'admin_slide.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formslide_admin(request):
    form = SlideForm()
    if request.method == 'POST':
        formsimpan = SlideForm(request.POST,request.FILES)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('slide_admin')
    context = {
        'judul': 'Halaman Form Slide',
        'menu': 'slide',
        'form':form
    }
    return render(request, 'admin_formslide.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editslide_admin(request, pk):
    slide = Slide.objects.get(id=pk)
    form = SlideForm(instance=slide)
    if request.method == 'POST':
        formsimpan = SlideForm(request.POST,request.FILES, instance=slide)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('slide_admin')
    context = {
       'judul': 'Halaman Form Edit Slide',
        'menu': 'slide',
        'form':form
    }
    return render(request, 'admin_formslide.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deleteslide_admin(request, pk):
    hapus = Slide.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('slide_admin')
    context = {
        'judul': 'Halaman Hapus Slide',
        'menu': 'slide',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusslide.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def pelanggan_admin(request):
    pelanggan = Pelanggan.objects.all()
    context = {
        'data': pelanggan,
        'judul': 'Halaman Pelanggan Wifi',
        'menu': 'pelanggan',
    }
    return render(request, 'admin_pelanggan.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formpelanggan_admin(request):
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
            return redirect('pelanggan_admin')
    context = {
        'judul': 'Halaman Form Pelanggan',
        'menu': 'pelanggan',
        'form':form,
        'formuser':formuser
    }
    return render(request, 'admin_formpelanggan.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editpelanggan_admin(request, pk):
    pelanggan = Pelanggan.objects.get(id=pk)
    user = User.objects.get(id=pelanggan.user.id)
    form = PelangganForm(instance=pelanggan)
    formuser = UserForm(instance=user)
    if request.method == 'POST':
        formsimpan = PelangganForm(request.POST,request.FILES, instance=pelanggan)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('pelanggan_admin')
    context = {
       'judul': 'Halaman Form Edit Pelanggan',
        'menu': 'pelanggan',
        'form':form,
        'formuser':formuser
    }
    return render(request, 'admin_formpelanggan.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletepelanggan_admin(request, pk):
    hapus = Pelanggan.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('pelanggan_admin')
    context = {
        'judul': 'Halaman Hapus Pelanggan',
        'menu': 'pelanggan',
        'hapus':hapus  
    }
    return render(request, 'admin_hapuspelanggan.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def perbaikan_admin(request):
    perbaikan = Perbaikan.objects.all()
    context = {
        'data': perbaikan,
       'judul': 'Halaman Perbaikan',
        'menu': 'transaksi',
    }
    return render(request, 'admin_perbaikan.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def formperbaikan_admin(request):
    form = PerbaikanForm()
    if request.method == 'POST':
        formsimpan = PerbaikanForm(request.POST,request.FILES)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('perbaikan_admin')
    context = {
        'judul': 'Halaman Form Perbaikan',
        'menu': 'transaksi',
        'form':form
    }
    return render(request, 'admin_formperbaikan.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editperbaikan_admin(request, pk):
    perbaikan = Perbaikan.objects.get(id=pk)
    form = PerbaikanForm(instance=perbaikan)
    if request.method == 'POST':
        formsimpan = PerbaikanForm(request.POST,request.FILES, instance=perbaikan)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('perbaikan_admin')
    context = {
       'judul': 'Halaman Form Edit Perbaikan',
        'menu': 'transaksi',
        'form':form
    }
    return render(request, 'admin_formperbaikan.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deleteperbaikan_admin(request, pk):
    hapus = Perbaikan.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('perbaikan_admin')
    context = {
        'judul': 'Halaman Hapus Perbaikan',
        'menu': 'transaksi',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusperbaikan.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def settingpembayaran(request):
    tahun = Tahun.objects.filter(aktif=True).order_by('-id')
    selesai = DetailPasang.objects.filter(status='Selesai').order_by('-id')
    tidakselesai = DetailPasang.objects.exclude(status='Selesai').order_by('-id')
    
    context = {
        'tahun': tahun,
        'judul': 'Halaman Setting Pembayaran',
        'menu': 'setting',
        'tidakselesai':tidakselesai,
        'selesai':selesai

    }
    return render(request, 'admin_setinggpembayaran.html', context)


@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def editpasang_admin(request, pk):
    pasang = DetailPasang.objects.get(id=pk)
    form = DetailPasangForm(instance=pasang)
    if request.method == 'POST':
        formsimpan = DetailPasangForm(request.POST,request.FILES, instance=pasang)
        if formsimpan.is_valid():
            formsimpan.save()
            return redirect('settingpembayaran')

            
    context = {
       'judul': 'Halaman Form Edit Pemasangan',
        'menu': 'setting',
        'form':form,
    }
    return render(request, 'admin_formpemasangan.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletepasang_admin(request, pk):
    hapus = DetailPasang.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('settingpembayaran')
    context = {
        'judul': 'Halaman Hapus Pemasangan',
        'menu': 'setting',
        'hapus':hapus  
    }
    return render(request, 'admin_hapuspasang.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def simpansettingpasang(request):
    if request.method == "POST":
        idpasang = request.POST.getlist('id[]')
        bulan = request.POST.get('bulan')
        tahun = request.POST.get('tahun')
       
        # auth_token = str(uuid.uuid4())
        # obe = Obe.objects.create(dosen=dosen,tahun_akademik=tahunakademik,token_aktifasi_obe=auth_token)
        # obe.save()
        for row in idpasang:
            iddetailpasang= DetailPasang.objects.get(pk=row)
            simpan = SettingPembayaran.objects.create(status='Baru')
            simpan.detailpasang = iddetailpasang
            simpan.tahun = tahun
            simpan.bulan = bulan
            simpan.save()
        return JsonResponse({'status': 'Save' })
    else:
        return JsonResponse({'status' : 0})

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def belumbayar_admin(request):
    belumbayar = SettingPembayaran.objects.exclude(status='Lunas').order_by('-id')
    context = {
        'data': belumbayar,
       'judul': 'Halaman Data Belum Bayar Bulanan',
        'menu': 'transaksi',
    }
    return render(request, 'admin_belumbayar.html', context)



@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletebelumbayar_admin(request, pk):
    hapus = SettingPembayaran.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('belumbayar_admin')
    context = {
        'judul': 'Halaman Data Hapus Belum Bayar Bulanan',
        'menu': 'transaksi',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusbelumbayar.html', context)

@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def bayar_admin(request):
    bayar = SettingPembayaran.objects.filter(status='Lunas').order_by('-id')
    context = {
        'data': bayar,
       'judul': 'Halaman Data  Bayar Bulanan',
        'menu': 'transaksi',
    }
    return render(request, 'admin_bayar.html', context)



@login_required(login_url='login_page')
@ijinkan_pengguna(yang_diizinkan=['administrator']) 
def deletebayar_admin(request, pk):
    hapus = SettingPembayaran.objects.get(id=pk)
    if request.method == 'POST':
        hapus.delete()
        return redirect('bayar_admin')
    context = {
        'judul': 'Halaman Data Hapus  Bayar Bulanan',
        'menu': 'transaksi',
        'hapus':hapus  
    }
    return render(request, 'admin_hapusbayar.html', context)