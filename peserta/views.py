from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from peserta.models import Peserta

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
    peserta = Peserta.objects.get(id=request.session['peserta_id'])
    return render(request, 'profil.html', {"peserta":peserta})
