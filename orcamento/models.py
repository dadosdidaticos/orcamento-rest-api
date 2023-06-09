from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=30)
    hiring_date=models.DateField(null=False)
    health_insurance_cost=models.DecimalField(decimal_places=2, max_digits=20)
    def __str__(self):
        return self.name

class Company(models.Model):
    class Meta:
        verbose_name_plural="Companies"

    name=models.CharField(max_length=30)
    cnpj=models.CharField(max_length=18)
    inss_aliquot=models.DecimalField(decimal_places=3, max_digits=20,null=False)
    def __str__(self):
        return self.name


class Department(models.Model):
    company=models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Scenario(models.Model):
    name=models.CharField(max_length=30, default='Teste')
    initial_period=models.DateField()
    end_period=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    last_modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EmployeeState(models.Model):

    CLT='C'
    PESSOA_JURIDICA='P'
    ESTAGIARIO='E'
    DIRETOR='D'
    RELATIONSHIPS_DICT = {'C':'CLT','P':'Pessoa Jurídica','E':'Estagiário','D':'Diretor Estatutário'}
    RELATIONSHIPS = (
        (CLT,'CLT'),
        (PESSOA_JURIDICA,'Pessoa Jurídica'),
        (ESTAGIARIO,'Estagiário'),
        (DIRETOR,'Diretor'),
    )

    ATIVO='A'
    PROJECAO='P'
    INATIVO='I'
    EMPLOYEE_TYPES_DICT = {'A':'Ativo','P':'Projeção','I':'Inativo'}
    EMPLOYEE_TYPES = (
        (ATIVO,"Ativo"),
        (PROJECAO,"Projeção"),
        (INATIVO,"Inativo")
    )
    employee=models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    scenario=models.ForeignKey(Scenario, on_delete=models.CASCADE, null=True)
    job=models.CharField(max_length=30)
    employee_type=models.CharField(max_length=1, choices=EMPLOYEE_TYPES, blank=False, null=False, default="A")
    relationship_type=models.CharField(max_length=1, choices=RELATIONSHIPS, blank=False, null=False, default="C")
    base_salary=models.DecimalField(decimal_places=2, max_digits=20)
    benefits=models.DecimalField(decimal_places=2, max_digits=20)
    performance_award=models.DecimalField(decimal_places=2, max_digits=20)
    commission=models.DecimalField(decimal_places=2, max_digits=20)
    initial_month=models.DateField()
    end_month=models.DateField()

    def __str__(self):
        return str(self.id)
    