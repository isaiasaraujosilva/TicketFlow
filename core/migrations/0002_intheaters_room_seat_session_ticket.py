# Generated by Django 4.1.7 on 2023-03-11 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InTheaters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=25)),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255)),
                ('avaliable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=10)),
                ('number', models.IntegerField()),
                ('available', models.BooleanField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.room')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day', models.DateField()),
                ('room_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.people')),
                ('seat_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.seat')),
                ('session_id', models.ManyToManyField(to='core.session')),
            ],
        ),
    ]
