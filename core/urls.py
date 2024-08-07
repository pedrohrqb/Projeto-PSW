from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Abaixo eu crio um caminho "usuarios", assim sendo necessario criar uma pasta "urls.py", no APP usuarios.
    path('usuarios/', include('usuarios.urls')),
    path('empresarios/', include('empresarios.urls')),
]
