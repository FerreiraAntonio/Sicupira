# Generated by Django 2.2.10 on 2020-03-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_auto_20200329_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abreviatura',
            name='flg_principal',
            field=models.BooleanField(default=False),
        ),
    ]
