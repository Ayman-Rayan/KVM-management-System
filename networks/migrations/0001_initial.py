# Generated by Django 4.0.5 on 2022-06-21 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'required': 'No pool name has been entered'}, max_length=20)),
                ('subnet', models.CharField(error_messages={'required': 'No subnet has been entered'}, max_length=20)),
                ('forward', models.CharField(max_length=100)),
                ('bridge_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Network',
            },
        ),
    ]
