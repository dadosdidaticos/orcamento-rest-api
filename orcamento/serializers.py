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
        fields = ['id','name','initial_period','end_period','created_at','last_modified_at']
        
class EmployeeStateSerializer(serializers.ModelSerializer):
    hiring_date=serializers.SerializerMethodField()
    health_insurance_cost=serializers.SerializerMethodField()

    class Meta:
        fields = ('id','employee','hiring_date','health_insurance_cost','department','scenario','job','employee_type','relationship_type','base_salary','benefits','performance_award','commission','initial_month','end_month')
        model = EmployeeState
    
    def get_hiring_date(self,obj):
        return obj.employee.hiring_date
    def get_health_insurance_cost(self,obj):
        return obj.employee.health_insurance_cost