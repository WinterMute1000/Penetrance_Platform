# Generated by Django 2.2.18 on 2021-06-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadWebShells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shell_name', models.CharField(max_length=2048)),
                ('code_or_url', models.CharField(max_length=100000)),
            ],
        ),
    ]
