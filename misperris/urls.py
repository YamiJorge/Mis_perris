
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.mascota.urls', namespace = "mascota")),
    url(r'^mascota/', include('apps.mascota.urls', namespace = "mascota")),
    url(r'^adopcion/', include('apps.adopcion.urls', namespace = "adopcion")),
]
