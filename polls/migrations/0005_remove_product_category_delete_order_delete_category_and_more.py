# Generated by Django 5.0.7 on 2024-08-01 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_category_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
