# Generated by Django 2.0.5 on 2019-01-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190103_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urllink',
            name='website',
            field=models.URLField(),
        ),
    ]
