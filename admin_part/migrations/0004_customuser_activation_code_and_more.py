# Generated by Django 5.1.1 on 2024-10-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_part', '0003_remove_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='activation_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='activation_code_created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reset_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
