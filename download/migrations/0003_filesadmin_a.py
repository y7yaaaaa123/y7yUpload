# Generated by Django 4.0.5 on 2022-07-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0002_remove_filesadmin_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesadmin',
            name='a',
            field=models.FileField(null=True, upload_to='media_cdn'),
        ),
    ]