# Generated by Django 4.2.5 on 2023-09-22 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jokes', '0008_alter_category_options_alter_tag_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
