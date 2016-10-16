from django.forms import ModelForm
from django import forms

from peserta.models import Peserta

class DaftarForm(ModelForm):
    class Meta:
        model = Peserta
        fields = ['nama','alamat','jenis_kelamin','no_telepon','email','minat','alasan']
        labels = {
            'nama':'Nama Lengkap',
            'alamat':'Alamat',
            'jenis_kelamin': 'Jenis Kelamin',
            'no_telepon':'No. Telp/HP',
            'email':'Email',
            'minat':'Sebutkan Minat Gabung IT Camp',
            'alasan':'Sebutkan Alasan Gabung IT Camp',
        }
        error_messages = {
            'nama': {
                'required': 'Masukan Nama Lengkap Anda'
            },
            'alamat': {
                'required': 'Masukan Alamat Anda'
            },
            'jenis_kelamin': {
                'required': 'Harus Di Isi'
            },
            'no_telepon': {
                'required': 'Harus Di Isis'
            },
            'email': {
                'required': 'Harus Di Isis'
            },
            'minat': {
                'required': 'Harus Di Isis'
            },
            'alasan': {
                'required': 'Harus Di Isis'
            },
        }
        widgets = {
            'nama':forms.TextInput(attrs={'class': 'form-control'}),
            'alamat':forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kelamin':forms.Select(attrs={'class': 'form-control'}),
            'no_telepon':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'minat':forms.Textarea(attrs={ 'cols':50, 'rows': 10, 'class': 'form-control'}),
            'alasan':forms.Textarea(attrs={ 'cols':50, 'rows': 10, 'class': 'form-control'}),
        }
