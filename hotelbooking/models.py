from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=264)
    def __str__(self):
        return self.customer_name

class Room(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    room = models.CharField(max_length=264)
    def __str__(self):
        return self.room

class AccessRecord(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return str(self.date)