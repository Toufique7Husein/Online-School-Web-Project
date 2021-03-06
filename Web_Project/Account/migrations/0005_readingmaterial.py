# Generated by Django 3.2.5 on 2021-08-22 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_delete_readingmaterial'),
        ('Account', '0004_auto_20210808_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('assignDate', models.DateTimeField(auto_now_add=True)),
                ('dueDate', models.DateField(blank=True)),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classroom.classroom')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Account.faculty')),
            ],
        ),
    ]
