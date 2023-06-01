from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orcamento.views import CompanyViewset, EmployeeViewset, ScenarioViewset, DepartmentViewset, EmployeeStateViewset
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Orçamento API",
      default_version='v1',
      description="API to serve the front-end application",
      terms_of_service="#",
      contact=openapi.Contact(email="marcosvcc@poli.urfj.br"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('companies', CompanyViewset, basename='Company')
router.register('employees', EmployeeViewset, basename='Employee')
router.register('scenarios', ScenarioViewset, basename='Scenario')
router.register('departments', DepartmentViewset, basename='Department')
router.register('employeeStates', EmployeeStateViewset, basename='EmployeeState')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('__debug__/', include('debug_toolbar.urls')),
]
