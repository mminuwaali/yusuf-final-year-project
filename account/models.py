from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

GENDER = [(i, i) for i in ["male", "female"]]


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Employee(models.Model):
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    employee = models.OneToOneField(User, models.CASCADE)
    gender = models.CharField(max_length=100, choices=GENDER)
    department = models.ForeignKey("landing.department", models.PROTECT)
    performance = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100)]
    )

    def __str__(self):
        return self.employee.username
