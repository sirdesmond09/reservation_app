# Generated by Django 3.2.13 on 2022-06-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
