from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
class Equipments(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    image=models.CharField(max_length=600)
    quantity = models.IntegerField()
    Mentor = models.CharField(max_length=30)
    MentorEmail = models.CharField(max_length=100)
    TotalTaken = models.IntegerField(default=0)

    def __str__(self):
        return self.name + '-' + self.Mentor

class EquipmentStatus(models.Model):
    name = models.ForeignKey(Equipments, on_delete=models.CASCADE)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, default='NULL')
    Status = models.IntegerField(default=0)
    Reason = models.CharField(max_length=1000,default="none")

    def __str__(self):
        return self.Reason
