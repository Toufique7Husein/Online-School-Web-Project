# Generated by Django 3.2.5 on 2021-08-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_readingmaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingmaterial',
            name='paper',
            field=models.FileField(blank=True, null=True, upload_to='read_material'),
        ),
    ]
