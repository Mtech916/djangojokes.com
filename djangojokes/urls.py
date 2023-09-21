from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Amdin
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    # User Management
    path("account/", include("allauth.urls")),
    # Local Apps
    path("jobs/", include("jobs.urls")),
    path("jokes/", include("jokes.urls")),
    path("", include("pages.urls")),
]
