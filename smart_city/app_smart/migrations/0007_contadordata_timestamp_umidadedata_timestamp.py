# Generated by Django 5.1.1 on 2024-10-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_smart', '0006_remove_contadordata_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contadordata',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='umidadedata',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
