from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from orcamento.models import Employee,EmployeeState, Scenario, Department, Company
from orcamento.serializers import DepartmentSerializer, EmployeeSerializer, EmployeeStateSerializer, ScenarioSerializer,CompanySerializer
from orcamento.models import EmployeeState
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class CompanyViewset(viewsets.ModelViewSet):
    """Exibe todas as empresas"""
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
class EmployeeViewset(viewsets.ModelViewSet):
    """Exibe todos os empregados cadastrados"""
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeStateViewset(viewsets.ModelViewSet):
    """Exibe todos os estados de empregados"""
    queryset=EmployeeState.objects.all()
    serializer_class=EmployeeStateSerializer

class ScenarioViewset(viewsets.ModelViewSet):
    """Exibe todos os cenários"""
    queryset=Scenario.objects.all()
    serializer_class=ScenarioSerializer

    @action(detail=True,methods=["GET"])
    def getCalculatedScenario(self, request, pk=None):
        qs_employee_state = EmployeeState.objects.filter(scenario=pk)
        scenario = Scenario.objects.filter(id=pk).first()
        df_scenario=scenario.get_employee_state_data_frame()
        serialized=EmployeeStateSerializer(qs_employee_state, many=True)
        return Response(serialized.data)

class DepartmentViewset(viewsets.ModelViewSet):
    """Exibe todos os departamentos"""
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
