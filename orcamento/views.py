from decimal import Decimal
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from orcamento.models import Employee,EmployeeState, Scenario, Department, Company
from orcamento.serializers import DepartmentSerializer, EmployeeSerializer, EmployeeStateSerializer, ScenarioSerializer,CompanySerializer
from orcamento.models import EmployeeState
from django_pandas.io import read_frame
import pandas as pd
import numpy as np
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
        """Realiza o Cálculo de impostos e valores para devolver o custo total por colaborador."""
        #obtaining the scenario from database:
        qs_scenario = EmployeeState.objects.select_related('employee').filter(scenario=pk)
        df_scenario = read_frame(qs_scenario,fieldnames=['id','employee__name','employee__hiring_date','employee__health_insurance_cost','department__company','department__company__inss_aliquot','department','scenario','job','employee_type','relationship_type','base_salary','benefits','performance_award','commission','initial_month','end_month'])

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

        #calculating fgts
        FGTS_ALIQUOT=Decimal(0.08)
        is_fgts_eligible=(df_scenario['employee_type']!='Inativo') & (df_scenario['relationship_type']=='CLT')
        df_scenario['fgts']=np.where(is_fgts_eligible, df_scenario['base_salary']*FGTS_ALIQUOT,0)

        #calculating Inss_patronal
        is_inss_eligible=(df_scenario['employee_type']!='Inativo') & ((df_scenario['relationship_type']=='CLT') | (df_scenario['relationship_type']=='Diretor Estaturário'))
        df_scenario['inss_patronal']=np.where(is_inss_eligible, df_scenario['base_salary']*df_scenario['department__company__inss_aliquot']/100,0)

        #calculating total comp
        df_scenario['total']=df_scenario[[
            'base_salary',
            'fgts',
            'inss_patronal',
            'employee__health_insurance_cost',
            'performance_award',
            'commission',
            'benefits'
        ]].sum(axis=1)

        return Response(data=json.loads(df_scenario.to_json(orient='records', lines=False)))

class DepartmentViewset(viewsets.ModelViewSet):
    """Exibe todos os departamentos"""
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
