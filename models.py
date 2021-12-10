from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.utils import timezone

# Create your models here.

class Dodaci(models.Model):
    naziv = models.TextField() 
    cijena = models.IntegerField()

    def __str__(self):
        return self.naziv


class Kava(models.Model):
    vrsta_kave =models.TextField()
    cijena = models.IntegerField()
    toplo_hladno =models.BooleanField(default=True)
    vrijeme_isporuke = models.TimeField()
    dodatak_u_kavu = models.ForeignKey(Dodaci, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{}".format(self.vrsta_kave, self.cijena)
        
        
class Stavka(models.Model):
    proizvod = models.CharField(max_length=20)
    kolicina = models.IntegerField()
    kava_vk = models.ForeignKey(Kava, on_delete=models.CASCADE)

    def __str__(self):
        return self.proizvod

class Salica(models.Model):
    boja = models.CharField(max_length=20)
    materijal = models.CharField(max_length=20)

    def __str__(self):
        return self.boja

class Narudzba(models.Model):
    broj_narudzbe = models.CharField(max_length=20, default="")
    ukupna_cijena = models.IntegerField()
    vKupnje = models.DateTimeField()
    broj_stavki = models.ManyToManyField(Stavka)
    naruzdba_vk=models.ForeignKey(Salica, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.broj_narudzbe)


