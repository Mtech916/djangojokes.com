from django.urls import path
from .views import HomePageView, AboutPageView

app_name = "pages"
urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about-us/", AboutPageView.as_view(), name="about-us"),
]
