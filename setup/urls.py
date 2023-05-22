from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orcamento.views import CompanyViewset, EmployeeViewset, ScenarioViewset, DepartmentViewset, EmployeeStateViewset

router = routers.DefaultRouter()
router.register('company', CompanyViewset, basename='Company')
router.register('employee', EmployeeViewset, basename='Employee')
router.register('scenario', ScenarioViewset, basename='Scenario')
router.register('department', DepartmentViewset, basename='Department')
router.register('employeeState', EmployeeStateViewset, basename='EmployeeState')
#router.register('execute', CalculateScenarioView, basename='execute')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
