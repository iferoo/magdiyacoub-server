# Generated by Django 3.2.13 on 2022-05-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_auto_20220518_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Diabeyic',
            field=models.BooleanField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Smoker',
            field=models.BooleanField(max_length=70, null=True),
        ),
    ]