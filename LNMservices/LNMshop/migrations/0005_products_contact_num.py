# Generated by Django 3.2.4 on 2021-06-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LNMshop', '0004_auto_20210611_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='contact_num',
            field=models.BigIntegerField(default=0),
        ),
    ]
