import os

from django.contrib import admin
from django.urls import path
from api.views import cadastro, inicio

urlpatterns = [
    path(os.getenv('ADMIN_URL', 'admin/'), admin.site.urls),

    path("", inicio, name="inicio"),
    path("api/cadastro/", cadastro, name="cadastro"),
]