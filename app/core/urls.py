from rest_framework.routers import DefaultRouter
from django.urls import path
from django.conf.urls import include
from .views import BeneficiarioViewSet
from .views import EmpleadoViewSet
from .views import EmpleadoProcedureViewSet
from .views import BeneficiarioProcedureViewSet

router = DefaultRouter()
router.register(r'empleado', EmpleadoViewSet, 'empleados')
router.register(r'beneficiario', BeneficiarioViewSet, 'beneficiario')
urlpatterns = [
    path(r'', include(router.urls)),
    path('empleados_procedure/',EmpleadoProcedureViewSet.as_view(), name="empleado_list_or_create"),
    path('empleados_procedure/<int:pk>/',EmpleadoProcedureViewSet.as_view(), name="empleado_get_or_update"),
    path('beneficiarios_procedure/',BeneficiarioProcedureViewSet.as_view(), name="beneficiario_list_or_create"),
    path('beneficiarios_procedure/<int:pk>/',BeneficiarioProcedureViewSet.as_view(), name="beneficiario_get_or_update"),
]