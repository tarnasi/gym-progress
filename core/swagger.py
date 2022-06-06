from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="GYM Program API",
      default_version='v1',
      description="Manage Athlete workouts with fully detail",
      terms_of_service="https://enigmastudio.dev/policies",
      contact=openapi.Contact(email="enigmastudio2022@gmail.com"),
      license=openapi.License(name="Private License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny, ),
)
