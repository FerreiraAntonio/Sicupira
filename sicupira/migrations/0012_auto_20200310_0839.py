# Generated by Django 3.0.3 on 2020-03-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sicupira', '0011_auto_20200310_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='flg_cooperacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='programa',
            name='flg_rede',
            field=models.BooleanField(default=False),
        ),
    ]