# Generated by Django 4.0.4 on 2022-06-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
