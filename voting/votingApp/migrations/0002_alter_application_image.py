# Generated by Django 4.0.1 on 2022-02-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='image',
            field=models.ImageField(upload_to='filepath'),
        ),
    ]
