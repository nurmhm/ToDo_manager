# Generated by Django 4.2.4 on 2023-08-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('statas', models.CharField(max_length=30)),
            ],
        ),
    ]
