# Generated by Django 4.2.6 on 2023-12-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0002_hirerequest_hirepackage_hires'),
    ]

    operations = [
        migrations.AddField(
            model_name='hirerequest',
            name='replied',
            field=models.BooleanField(default=False),
        ),
    ]
