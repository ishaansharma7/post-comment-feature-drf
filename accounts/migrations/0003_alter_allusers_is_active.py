# Generated by Django 4.0.2 on 2022-03-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_allusers_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusers',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]