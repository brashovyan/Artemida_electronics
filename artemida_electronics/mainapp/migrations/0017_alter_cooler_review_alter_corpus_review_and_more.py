# Generated by Django 4.1.2 on 2022-11-01 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_cooler_review_alter_corpus_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooler',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='corpus',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='hdd',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='power_block',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='ssd_m2',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='ssd_sata',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='videocard',
            name='review',
            field=models.ManyToManyField(blank=True, to='mainapp.review'),
        ),
    ]