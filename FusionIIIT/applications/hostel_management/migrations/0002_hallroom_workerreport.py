# Generated by Django 3.1.5 on 2021-05-11 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_id', models.CharField(max_length=10)),
                ('worker_name', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=2020)),
                ('month', models.IntegerField(default=1)),
                ('absent', models.IntegerField(default=0)),
                ('total_day', models.IntegerField(default=31)),
                ('remark', models.CharField(max_length=100)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
            ],
        ),
        migrations.CreateModel(
            name='HallRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=4)),
                ('block_no', models.CharField(max_length=1)),
                ('room_cap', models.IntegerField(default=3)),
                ('room_occupied', models.IntegerField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall')),
            ],
        ),
    ]