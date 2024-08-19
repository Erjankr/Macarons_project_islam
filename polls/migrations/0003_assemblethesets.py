# Generated by Django 5.0.7 on 2024-07-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_giftset_alter_sweetdays_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assemblethesets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Собрать набор',
                'verbose_name_plural': 'Собрать набор',
            },
        ),
    ]