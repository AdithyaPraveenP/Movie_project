# Generated by Django 4.2.11 on 2024-03-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_userdata_email_userdata_password1_userdata_password2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='dp',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
