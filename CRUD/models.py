from django.db import models

# Create your models here.
class User(models.Model):
  userId = models.AutoField(primary_key=True, default=None)
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  department = models.CharField(max_length=100)
  contact = models.IntegerField()
  role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Visitor', 'Visitor'),], default= 'Visitor')