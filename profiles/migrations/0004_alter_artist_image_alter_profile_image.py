# Generated by Django 5.0.6 on 2024-07-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_specs_alter_artist_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(default='images/avatar_ndcfzk.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/avatar_ndcfzk.png', upload_to='images/'),
        ),
    ]
