from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from authenticate.views import DashboardView

urlpatterns = [
    path('dashboard/admin/', admin.site.urls),
    path('auth/', include('authenticate.urls', namespace="authenticate")),
    path('', DashboardView.as_view(), name="home-page"),
    path('gym/', include('gym.urls', namespace="GYM"))
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
