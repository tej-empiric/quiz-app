# Generated by Django 5.0.4 on 2024-04-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_attempted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempted',
            name='choice',
            field=models.CharField(max_length=150),
        ),
    ]
