from django.db import models

# Create your models here.



class ContactModel1(models.Model):
    subject = models.CharField(max_length=100)
    sender = models.EmailField()

class ContactModel2(models.Model):
    message = models.CharField(max_length=100)
