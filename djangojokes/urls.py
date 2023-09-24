from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Amdin
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    # User Management
    path("account/", include("users.urls")),
    path("account/", include("allauth.urls")),
    # Local Apps
    path("jobs/", include("jobs.urls")),
    path("jokes/", include("jokes.urls")),
    path("", include("pages.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
