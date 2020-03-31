from django.db import models


class User(models.Model):
    SEX = (
        ('0', '男'),
        ('1', '女')
    )
    id = models.IntegerField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=20, help_text="用户名")
    password = models.CharField(max_length=32, help_text="密码")
    sex = models.IntegerField(choices=SEX, null=True, blank=True)

    def __str__(self):
        return (self.name)
