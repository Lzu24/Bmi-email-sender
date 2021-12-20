from django.db import models

class BmiMeasurement(models.Model):
    height_in_meters = models.FloatField()
    weight_in_kg = models.FloatField()

    def bmi(self):
        return self.weight_in_kg / self.height_in_meters ** 2


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    subject = models.TextField()

    def __str__(self):
        return self.name