"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from agronegocio.views import (
    PropriedadeViewSet, CulturaViewSet, FuncionarioViewSet,
    FornecedorViewSet, InsumoViewSet, PlantioViewSet,
    HistoricoPlantioViewSet, ColheitaViewSet
)

router = routers.DefaultRouter()
router.register(r'propriedades', PropriedadeViewSet)
router.register(r'culturas', CulturaViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'insumos', InsumoViewSet)
router.register(r'plantios', PlantioViewSet)
router.register(r'historicos-plantio', HistoricoPlantioViewSet)
router.register(r'colheitas', ColheitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
