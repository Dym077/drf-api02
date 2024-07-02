# Generated by Django 5.0.6 on 2024-06-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(default='../avatar_ndcfzk.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/default_profile_relxos.jpg', upload_to='images/'),
        ),
    ]