from django.contrib import admin
from orcamento.models import Department, Company, Scenario, Employee, EmployeeState

class Departamentos(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Department, Departamentos)

class Empresas(admin.ModelAdmin):
    list_display = ('id','name','cnpj','inss_aliquot')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Company, Empresas)

class Empregados(admin.ModelAdmin):
    list_display = ('id','name','hiring_date','health_insurance_cost',)
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Employee, Empregados)

class Cenarios(admin.ModelAdmin):
    list_display = ('id','name','initial_period','end_period','created_at','last_modified_at')
    list_display_links = ('id','name',)
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Scenario, Cenarios)

class Orcamento(admin.ModelAdmin):
    list_display = ('id','scenario','employee','employee_type','relationship_type','department','base_salary','benefits','performance_award','commission','initial_month','end_month')
    list_display_links = ('id',)
    search_fields = ('scenario',)
    list_per_page = 20

admin.site.register(EmployeeState, Orcamento)

