# Generated by Django 2.2.3 on 2020-12-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0007_auto_20201213_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='income',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]