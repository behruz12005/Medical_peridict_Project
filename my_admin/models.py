from django.db import models

# Create your models here.

class MyModel(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    file = models.FileField(upload_to='file/')


from django.db import models

class AnalyzResult(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    buying = models.IntegerField()
    systolic_blood_pressure = models.IntegerField()
    total_cholesterol = models.IntegerField()
    hdl_cholesterol = models.IntegerField()
    on_blood_pressure_medication = models.CharField(max_length=10)
    cigarette_smoker = models.CharField(max_length=10)
    diabetes_present = models.CharField(max_length=10)
    predict = models.CharField(max_length=100)



