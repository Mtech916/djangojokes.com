# Generated by Django 4.2.5 on 2023-09-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
