from rest_framework import viewsets
from orcamento.models import Employee,EmployeeState, Scenario, Department, Company
from orcamento.serializers import DepartmentSerializer, EmployeeSerializer, EmployeeStateSerializer, ScenarioSerializer,CompanySerializer

class CompanyViewset(viewsets.ModelViewSet):
    """Exibe todos as empresas"""
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
class EmployeeViewset(viewsets.ModelViewSet):
    """Exibe todos as empresas"""
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeStateViewset(viewsets.ModelViewSet):
    """Exibe todos as empresas"""
    queryset=EmployeeState.objects.all()
    serializer_class=EmployeeStateSerializer

class ScenarioViewset(viewsets.ModelViewSet):
    """Exibe todos as empresas"""
    queryset=Scenario.objects.all()
    serializer_class=ScenarioSerializer

class DepartmentViewset(viewsets.ModelViewSet):
    """Exibe todos as empresas"""
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer


