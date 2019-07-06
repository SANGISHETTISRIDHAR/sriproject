from django.db import models

class Client(models.Model):
    name=models.CharField(max_length=30)
    contact_no=models.IntegerField()
    photo=models.ImageField(upload_to='client/')
    address=models.TextField()
    client_un=models.CharField(max_length=30,primary_key=True)
    client_pwd=models.CharField(max_length=30)
    otp=models.IntegerField()

class Complaint(models.Model):
    no=models.AutoField(primary_key=True)
    client_un=models.ForeignKey(Client,on_delete=models.CASCADE)
    comment=models.TextField()