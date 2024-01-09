# Generated by Django 4.2.8 on 2024-01-08 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0025_journal_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referencenumbercounter',
            old_name='counter',
            new_name='next_reference_no',
        ),
        migrations.AlterField(
            model_name='referencenumbercounter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
