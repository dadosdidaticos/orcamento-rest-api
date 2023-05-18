from rest_framework import serializers
from orcamento.models import Employee,EmployeeState, Scenario, Department, Company

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','hiring_date','health_insurance_cost']
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','cnpj']
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name','company']
        
class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ['id','initial_period','end_period','created_at','last_modified_at']
        
class EmployeeStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeState
        fields = ['id','employee','department','scenario','job','base_salary','benefits','performance_award','commission','initial_month','end_month']