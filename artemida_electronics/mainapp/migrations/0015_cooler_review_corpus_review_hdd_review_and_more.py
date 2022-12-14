# Generated by Django 4.1.2 on 2022-11-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooler',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
        migrations.AddField(
            model_name='corpus',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
        migrations.AddField(
            model_name='hdd',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
        migrations.AddField(
            model_name='power_block',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
        migrations.AddField(
            model_name='ram',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
        migrations.AddField(
            model_name='ssd_m2',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
        migrations.AddField(
            model_name='ssd_sata',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='review',
            field=models.ManyToManyField(to='mainapp.review'),
        ),
    ]
