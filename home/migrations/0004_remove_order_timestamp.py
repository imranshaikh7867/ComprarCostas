# Generated by Django 4.0.1 on 2022-07-02 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='timestamp',
        ),
    ]
