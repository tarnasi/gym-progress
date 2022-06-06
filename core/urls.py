from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .swagger import schema_view

urlpatterns = [
    path('portal', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    # swagger
    path(r'docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # apps urls
    path('api/user/', include('authenticate.urls', namespace="authenticate")),
    path('api/program/', include('program.urls', namespace="program")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
