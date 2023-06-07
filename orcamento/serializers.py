from rest_framework import serializers
from orcamento.models import Employee,EmployeeState, Scenario, Department, Company

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','hiring_date','health_insurance_cost']
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','cnpj','inss_aliquot']
        
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
    department_name=serializers.SerializerMethodField()
    company_name=serializers.SerializerMethodField()
    company=serializers.SerializerMethodField()
    employee_name=serializers.SerializerMethodField()
    
    relationship_type_name = serializers.SerializerMethodField(
        read_only=True)
    employee_type_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = ('id','employee','employee_name','hiring_date','health_insurance_cost','department','department_name','company','company_name','scenario','job','employee_type','employee_type_name','relationship_type','relationship_type_name','base_salary','benefits','performance_award','commission','initial_month','end_month')
        model = EmployeeState
    
    def get_hiring_date(self,obj):
        return obj.employee.hiring_date
    def get_health_insurance_cost(self,obj):
        return obj.employee.health_insurance_cost
    def get_employee_type_name(self, obj):
        return obj.EMPLOYEE_TYPES_DICT[obj.employee_type]
    def get_relationship_type_name(self, obj):
        return obj.RELATIONSHIPS_DICT[obj.relationship_type]
    def get_department_name(self,obj):
        return obj.department.name
    def get_company_name(self,obj):
        return obj.department.company.name
    def get_company(self,obj):
        return obj.department.company.id
    def get_employee_name(self,obj):
        return obj.employee.name