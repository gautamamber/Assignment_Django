# Generated by Django 2.0.2 on 2018-10-12 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
