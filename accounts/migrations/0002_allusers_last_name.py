# Generated by Django 4.0.2 on 2022-03-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allusers',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
