# Generated by Django 2.2.7 on 2019-12-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodos', '0002_auto_20191206_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
