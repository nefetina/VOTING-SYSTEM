# Generated by Django 4.0.4 on 2022-07-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingApp', '0002_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vote', models.IntegerField(max_length=10)),
            ],
        ),
    ]
