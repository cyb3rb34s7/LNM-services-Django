from django.db import models
from accounts.models import Accounts
import random
# Create your models here.


class Blog(models.Model):

    pickup = models.CharField(max_length=100, null=False, default='')
    drop = models.CharField(max_length=100, null=False, default='')
    username = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, null=False, default='')
    space = models.IntegerField(null=False, default=0)
    contact_num = models.BigIntegerField(null=False, default=0)
    fare = models.IntegerField(null=False, default=0)
    date = models.DateTimeField(null=False)
    time = models.TimeField(null=False)
    color = models.CharField(max_length=20, default='bg-dark')

    @staticmethod
    def get_random_colour():
        l = ["bg-primary", "bg-secondary", "bg-success", "bg-danger",
             "bg-warning", "bg-info", "bg-dark"]
        x = random.randint(0, 6)
        return (l[x])
