# Generated by Django 3.0.5 on 2020-12-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20201206_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executecmd',
            name='raw_cmd',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
