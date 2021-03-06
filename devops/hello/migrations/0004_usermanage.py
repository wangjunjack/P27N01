# Generated by Django 2.2 on 2020-03-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20200331_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='用户名', max_length=20)),
                ('sex', models.IntegerField(blank=True, choices=[('0', '男'), ('1', '女')], default=0, help_text='性别')),
                ('passwd', models.CharField(help_text='密码', max_length=32)),
            ],
        ),
    ]
