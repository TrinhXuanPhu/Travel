# Generated by Django 4.1.4 on 2023-01-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdulich', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_img',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='media', verbose_name='Feature Image'),
        ),
    ]
