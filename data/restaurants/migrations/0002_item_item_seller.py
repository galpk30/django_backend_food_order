# Generated by Django 5.0 on 2023-12-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_seller',
            field=models.PositiveIntegerField(default=1),
        ),
    ]