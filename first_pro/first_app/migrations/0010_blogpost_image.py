# Generated by Django 3.2.3 on 2021-05-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_alter_blogpost_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
