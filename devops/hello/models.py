from django.db import models


class User(models.Model):
    SEX = (
        ('0', '男'),
        ('1', '女')
    )
    id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=20, help_text="用户名")
    sex = models.IntegerField(choices=SEX, null=False, blank=True, default=0, help_text="性别")
    passwd = models.CharField(max_length=32, help_text='密码')

    def __str__(self):
        return (self.username)
