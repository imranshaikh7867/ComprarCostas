# Generated by Django 4.0.1 on 2022-07-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_orderupdate_update_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
    ]