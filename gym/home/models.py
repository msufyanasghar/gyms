from django.db import models


class HomePageContent(models.Model):
    logo = models.ImageField(upload_to="home/logo")
    class Meta:
        verbose_name_plural = "Home Page "


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Contact"

