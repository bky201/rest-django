# Generated by Django 4.2.4 on 2023-09-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_bxensm', upload_to='images/'),
        ),
    ]