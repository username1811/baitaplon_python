# Generated by Django 4.2.5 on 2023-09-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_profile_address_profile_phonenumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(blank=True, default='user', max_length=50, null=True),
        ),
    ]
