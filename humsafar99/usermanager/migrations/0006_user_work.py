# Generated by Django 2.2.3 on 2020-12-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0005_auto_20201213_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Work',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
