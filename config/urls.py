from django.contrib import admin
from django.urls import path
from api.views import cadastro, inicio

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("api/cadastro/", cadastro, name="cadastro"),
]