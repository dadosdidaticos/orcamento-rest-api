from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orcamento.views import CompanyViewset, EmployeeViewset, ScenarioViewset, DepartmentViewset, EmployeeStateViewset

router = routers.DefaultRouter()
router.register('companies', CompanyViewset, basename='Company')
router.register('employees', EmployeeViewset, basename='Employee')
router.register('scenarios', ScenarioViewset, basename='Scenario')
router.register('departments', DepartmentViewset, basename='Department')
router.register('employeeStates', EmployeeStateViewset, basename='EmployeeState')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('__debug__/', include('debug_toolbar.urls')),
]
