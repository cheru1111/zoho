# Generated by Django 4.2.8 on 2024-01-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0029_journalrecievedidmodel_delete_lastdeletedreference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalrecievedidmodel',
            name='ref_number',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]
