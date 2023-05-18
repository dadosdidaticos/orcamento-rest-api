from django.db import models
from uuid import uuid4

class Employee(models.Model):
    name=models.CharField(max_length=30)
    hiring_date=models.DateField(null=False)
    health_insurance_cost=models.DecimalField(decimal_places=2, max_digits=20)


class Company(models.Model):
    name=models.CharField(max_length=30)
    cnpj=models.CharField(max_length=18)


class Department(models.Model):
    company=models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=30)

class Scenario(models.Model):
    initial_period=models.DateField()
    end_period=models.DateField()


class EmployeeState(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    scenario=models.ForeignKey(Scenario, on_delete=models.SET_NULL, null=True)
    job=models.CharField(max_length=30)
    base_salary=models.DecimalField(decimal_places=2, max_digits=20)
    benefits=models.DecimalField(decimal_places=2, max_digits=20)
    performance_award=models.DecimalField(decimal_places=2, max_digits=20)
    commission=models.DecimalField(decimal_places=2, max_digits=20)
    initial_month=models.DateField()
    end_month=models.DateField()


