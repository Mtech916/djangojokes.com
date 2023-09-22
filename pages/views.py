from django.contrib import messages
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about-us.html"

    # def get(self, request, *args, **kwargs):
    #     messages.debug(request, "Debug message.")
    #     messages.info(request, "Info message.")
    #     messages.success(request, "Success message.")
    #     messages.warning(request, "Warning message.")
    #     messages.error(request, "Error message.")
    #     return super().get(request, args, kwargs)
