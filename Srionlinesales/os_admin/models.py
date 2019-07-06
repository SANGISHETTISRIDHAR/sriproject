from django.db import models

class Adminlogin(models.Model):
    contactno=models.IntegerField(primary_key=True)
    password=models.CharField(max_length=20)
    otp=models.IntegerField()


class Agent(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='agent/')
    address=models.TextField()
    agent_un=models.CharField(primary_key=True,max_length=30)
    agent_pwd=models.CharField(max_length=30)
    contactno=models.IntegerField()
    otp=models.IntegerField()
