# Generated by Django 2.2.18 on 2021-05-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformationDisclosureLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=2048)),
                ('scan_date', models.DateTimeField(auto_now=True)),
                ('result', models.TextField()),
            ],
        ),
    ]
