# Generated by Django 4.2.8 on 2023-12-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0017_alter_journal_reference_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='reference_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
