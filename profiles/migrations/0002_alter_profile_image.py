# Generated by Django 5.0.6 on 2024-07-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/default_profile_relxos', upload_to='images/'),
        ),
    ]
