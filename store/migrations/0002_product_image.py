# Generated by Django 2.2.28 on 2023-03-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
