# Generated by Django 5.1.1 on 2024-09-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='type',
            field=models.CharField(choices=[('Temperatura', 'Temperatura'), ('Umidade', 'Umidade'), ('Contador', 'Contador'), ('Luminosidade', 'Luminosidade')], max_length=50),
        ),
    ]
