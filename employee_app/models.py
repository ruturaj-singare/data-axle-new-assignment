from django.db import models
from utils.constants import *

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    birth_date = models.DateField()
    department = models.ForeignKey(Department,related_name=EMPLOYEE_DEPARTMENT_MODEL_MANAGER, on_delete=models.CASCADE)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.birth_date}"

class Address(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name=ADDRESS_EMPLOYEE_MODEL_MANAGER)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} Address"
