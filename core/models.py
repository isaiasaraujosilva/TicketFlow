from django.db import models

# Create your models here.
class People(models.Model):

    cpf = models.CharField(max_length=11)
    fires_name = models.CharField()
    last_name = models.CharField()
    sex = models.CharField()
    birth_date = models.DateField()
    phone_number = models.CharField()
    email = models.CharField()

