# Generated by Django 4.2.5 on 2023-09-20 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0006_tag_joke_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joke',
            old_name='tag',
            new_name='tags',
        ),
    ]
