# Generated by Django 2.2.3 on 2020-12-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0003_user_profilefor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Work',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='caste',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='color',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='diet',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='disability',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='familystatus',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='familytype',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='familyvalue',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.FloatField(default=0.0, max_length=5),
        ),
        migrations.AddField(
            model_name='user',
            name='qualification',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='religion',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.FloatField(default=0.0, max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]