# Generated by Django 2.1.2 on 2018-10-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=255)),
                ('write_date', models.DateTimeField()),
            ],
        ),
    ]