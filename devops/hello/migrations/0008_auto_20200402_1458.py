# Generated by Django 2.2 on 2020-04-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20200401_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
