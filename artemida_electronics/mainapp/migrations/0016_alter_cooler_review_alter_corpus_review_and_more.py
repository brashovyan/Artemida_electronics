# Generated by Django 4.1.2 on 2022-11-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_cooler_review_corpus_review_hdd_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooler',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='corpus',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='hdd',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='power_block',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='ram',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='ssd_m2',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='ssd_sata',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
        migrations.AlterField(
            model_name='videocard',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='mainapp.review'),
        ),
    ]
