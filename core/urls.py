from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Abaixo eu crio um caminho "usuarios", assim sendo necessario criar uma pasta "urls.py", no APP usuarios.
    path('usuarios/', include('usuarios.urls')),
    path('empresarios/', include('empresarios.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
