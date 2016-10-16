from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from peserta.models import Akun, Peserta
from homepage.forms import DaftarForm

# Create your views here.
def index_view(request):
    return render(request, 'new/index.html')

def daftar_view(request):
    if request.method == 'POST':
        form_data = request.POST
        form = DaftarForm(form_data)
        if form.is_valid():
            peserta = Peserta(

                )
            peserta.save()
            return redirect('/')
    else:
        form = DaftarForm()
    return render(request, 'new/daftar_peserta.html',{'form':form})

def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = Akun.objects.get(akun=user.id)
                    login(request, user)

                    request.session['peserta_id'] = akun.peserta_id
                    request.session['jenis_akun'] = akun.jenis_akun
                    request.session['username'] = request.POST['username']
                except:
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data Peserta, silahkan hubungi administrator')
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

    return render(request, 'new/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')
