from django.db import models


# Create your models here.
class cms(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    sex = models.CharField(max_length=40)
    number = models.IntegerField()

    def __str__(self):
        return self.firstName + ' ' + self.lastName