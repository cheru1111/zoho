# Generated by Django 4.2.8 on 2023-12-18 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0009_remove_journal_journal_journalentry_journal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalentry',
            name='journal',
        ),
        migrations.AddField(
            model_name='journal',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.journalentry'),
        ),
    ]