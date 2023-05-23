from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.renderers import JSONRenderer
from orcamento.models import Employee,EmployeeState, Scenario, Department, Company
from orcamento.serializers import DepartmentSerializer, EmployeeSerializer, EmployeeStateSerializer, ScenarioSerializer,CompanySerializer
from orcamento.models import EmployeeState
from rest_framework.response import Response
import pandas as pd
import json

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
        
        #obtaining the scenario from database:
        serializer = EmployeeStateSerializer(EmployeeState.objects.select_related('employee').filter(scenario=pk), many=True)
        df_scenario = pd.read_json(JSONRenderer().render(serializer.data).decode("utf-8"))
        
        #expanding month intervals into a list:
        to_be_exploded=df_scenario[['initial_month','end_month']]
        to_be_exploded = to_be_exploded.apply(lambda x: 
                                           pd.date_range(x.initial_month,x.end_month,freq='MS')
                                           .strftime("%Y-%m-%d")
                                           .tolist(),
                                           axis=1
                                        )
        to_be_exploded.name='month'

        #expanding
        df_scenario=pd.concat([df_scenario,to_be_exploded],axis=1)
        df_scenario.drop(['initial_month','end_month'], axis=1, inplace=True)
        df_scenario=df_scenario.explode('month')

        #return Response(data=json.loads(serializer.data))
        return Response(data=json.loads(df_scenario.to_json(orient='records', lines=False)))

class DepartmentViewset(viewsets.ModelViewSet):
    """Exibe todos os departamentos"""
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
