from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from CarSansar import settings

urlpatterns = [
    path("admin/", admin.site.urls),                        # django's admin panel url
    path("", include("app.urls")),                          # home page
    path("authentication/", include("auth.urls")),          # authentication app
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
