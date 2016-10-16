from django.contrib import admin
from peserta.models import *

# Register your models here.

class PesertaAdmin (admin.ModelAdmin):
    list_display = ['nama', 'alamat','jenis_kelamin','no_telepon','email','minat','alasan','waktu_daftar','status_regis']
    list_filter = ('nama','jenis_kelamin')
    search_fields = ['', '']
    list_per_page = 25
    actions=['regis_peserta', 'batal_regis_peserta']

    def regis_peserta(self, request, queryset):
        queryset.update(status_regis=True)
    regis_peserta.short_description = "Registrasi Peserta"

    def batal_regis_peserta(self, request, queryset):
        queryset.update(status_regis=False)
    batal_regis_peserta.short_description = "Batalkan Registrasi Peserta"

admin.site.register(Peserta, PesertaAdmin)

class AkunAdmin (admin.ModelAdmin):
    list_display = ['akun', 'peserta', 'jenis_akun']
    list_filter = ('jenis_akun',)
    search_fields = []
    list_per_page = 25

admin.site.register(Akun, AkunAdmin)
