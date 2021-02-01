from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from usermanager import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('', include('usermanager.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
