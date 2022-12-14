# Generated by Django 4.0.5 on 2022-06-21 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('networks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kvmm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'required': 'No Virtual Machine name has been entered'}, max_length=20)),
                ('vcpus', models.IntegerField(error_messages={'required': 'No VCPU has been entered'})),
                ('disk', models.IntegerField()),
                ('memory', models.IntegerField(error_messages={'required': 'No RAM size has been entered'})),
                ('storage', models.CharField(max_length=200)),
                ('iso', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('hdd_size', models.IntegerField()),
                ('mac', models.CharField(blank=True, default='52:54:00:25:fc:b8', max_length=200)),
                ('kvmcreator', models.IntegerField(default=1, verbose_name='kvm creator')),
                ('networks', models.ForeignKey(blank=True, default='network', on_delete=django.db.models.deletion.CASCADE, to='networks.network')),
            ],
            options={
                'verbose_name_plural': 'Kvm',
            },
        ),
        migrations.CreateModel(
            name='Kvm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'required': 'No Virtual Machine name has been entered'}, max_length=20)),
                ('vcpus', models.IntegerField(error_messages={'required': 'No VCPU has been entered'})),
                ('disk', models.IntegerField()),
                ('memory', models.IntegerField(error_messages={'required': 'No RAM size has been entered'})),
                ('storage', models.CharField(max_length=200)),
                ('iso', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('hdd_size', models.IntegerField()),
                ('mac', models.CharField(blank=True, default='52:54:00:25:fc:b8', max_length=200)),
                ('kvmcreator', models.IntegerField(default=1, verbose_name='kvm creator')),
                ('networks', models.ForeignKey(blank=True, default='network', on_delete=django.db.models.deletion.CASCADE, to='networks.network')),
            ],
            options={
                'verbose_name_plural': 'NET',
            },
        ),
    ]
