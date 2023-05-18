from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orcamento.views import CompanyViewset, EmployeeViewset, ScenarioViewset, DepartmentViewset, EmployeeStateViewset

router = routers.DefaultRouter()
router.register('Company', CompanyViewset, basename='Company')
router.register('Employee', EmployeeViewset, basename='Employee')
router.register('Scenario', ScenarioViewset, basename='Scenario')
router.register('Department', DepartmentViewset, basename='Department')
router.register('EmployeeState', EmployeeStateViewset, basename='EmployeeState')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
