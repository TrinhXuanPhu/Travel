# Generated by Django 4.1.4 on 2023-01-04 11:35

import ckeditor.fields
from django.db import migrations
from django import forms
  

class Migration(migrations.Migration):

    dependencies = [
        ('webdulich', '0005_post_post_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
