# Generated by Django 4.1.7 on 2023-05-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='image_name',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
