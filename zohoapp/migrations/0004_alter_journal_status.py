# Generated by Django 4.2.3 on 2023-11-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0003_delete_expensebyemployee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('save', 'Save')], default='draft', max_length=10),
        ),
    ]
