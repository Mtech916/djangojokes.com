# Generated by Django 4.2.5 on 2023-09-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0007_rename_tag_joke_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tag']},
        ),
        migrations.AlterField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(blank=True, to='jokes.tag'),
        ),
    ]