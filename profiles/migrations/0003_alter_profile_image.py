# Generated by Django 5.0.6 on 2024-07-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile_relxos.jpg', upload_to='images/'),
        ),
    ]
