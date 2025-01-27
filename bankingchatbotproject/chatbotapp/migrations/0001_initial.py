# Generated by Django 5.0.2 on 2024-02-14 22:04

import chatbotapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('customerAccountNo', chatbotapp.models.ThreeDigitAutoPrimaryKeyField(editable=False, primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=40)),
                ('authCode', models.IntegerField(default=576042)),
                ('balance', models.FloatField()),
            ],
        ),
    ]
