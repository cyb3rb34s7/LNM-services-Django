from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from accounts.models import Accounts


class Products(models.Model):

    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.BigIntegerField()
    username = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='products_imgs', blank=True, null=True)
    contact_num = models.BigIntegerField(default=0)


class Wishlist(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    username = models.ForeignKey(Accounts, on_delete=models.CASCADE, null=False)