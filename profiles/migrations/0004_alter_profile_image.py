# Generated by Django 5.0.6 on 2024-07-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='.../default_profile_relxos', upload_to='images/'),
        ),
    ]
