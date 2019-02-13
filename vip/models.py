from django.db import models

# Create your models here.

class User_Vip(models.Model):
    uid = models.IntegerField(max_length=255,verbose_name='用户id')
    u_grade = models.IntegerField(max_length=30,verbose_name='用户的vip等级')


class Vip(models.Model):
    grade = models.IntegerField(max_length=30,verbose_name='vip等级')
    v_power = models.CharField(max_length=50,verbose_name='vip的权限')

class Power(models.Model):
    Power_name = models.CharField(max_length=50,verbose_name='权限的描述')

