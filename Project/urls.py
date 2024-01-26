
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from Tienda import views
from Tienda.views import home, registro , hombre, mujer, logout_view, contacto, compra
from django.conf.urls.static import static

# Importa DEBUG desde settings
DEBUG = settings.DEBUG
urlpatterns = [
    # Home y Admin el home incluye los productos
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('contacto/', contacto, name="contacto"),
    # Vistas de productos para hombre y mujer 
    path('hombre/', hombre, name="hombre"),
    path('mujer/', mujer, name="mujer"),
    # Registrase y Login
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro, name="registro"),
    path('logout/', logout_view, name='logout'),
   # Comprar
    path('compra/', compra, name='compra'),
    
]
# Configuración para servir archivos de medios durante el desarrollo
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



