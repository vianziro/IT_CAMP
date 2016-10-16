from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Peserta (models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('p', 'Pria'),
        ('w', 'Wanita'),
    )
    nama = models.CharField(max_length=100)
    alamat = models.TextField(blank=True)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)
    no_telepon = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    minat=models.TextField()
    alasan= models.TextField()
    waktu_daftar= models.DateField()
    status_regis = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nama

class Akun (models.Model):
    JENIS_AKUN_CHOICES = (
        ('peserta', 'Peserta'),
        ('admin', 'Administrator'),
    )

    akun = models.ForeignKey(User)
    peserta = models.ForeignKey(Peserta)
    jenis_akun = models.CharField(max_length=20, choices=JENIS_AKUN_CHOICES)

    def __unicode__(self):
        return self.peserta.nama
