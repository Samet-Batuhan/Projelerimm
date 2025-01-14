from django.db import models
from .utils import get_link_data


class Category(models.Model):
    name = models.CharField(max_length=100)

class OneCikan(models.Model):
    kisi_adi = models.CharField(max_length=200)
    kisi_aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)

class Sair(models.Model):
    sair_adi = models.CharField(max_length=200)
    sair_aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)

class Muzisyen(models.Model):
    muzisyen_adi = models.CharField(max_length=200)
    muzisyen_aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)
 
class Sporcu(models.Model):
    sporcu_adi = models.CharField(max_length=200)
    sporcu_aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)

class Oyuncu(models.Model):
    oyuncu_adi = models.CharField(max_length=200)
    oyuncu_aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)

class Tarihci(models.Model):
    tarihci_adi = models.CharField(max_length=200)
    tarihci_aciklama = models.TextField()
    resim = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)



class Link(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField(blank=True)
    current_price = models.FloatField(blank=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('price_difference', '-created')

    def save(self, *args, **kwargs):
        name, price = get_link_data(self.url)
        old_price = self.current_price
        if self.current_price:
            if price != old_price:
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price
        else:
            self.old_price = 0
            self.price_difference = 0
        
        self.name = name
        self.current_price = price
        
        super().save(*args, **kwargs)