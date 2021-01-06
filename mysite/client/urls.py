from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("data",views.data,name = "data"),
    path("download",views.download,name = "download"),
    path("top3_view",views.top3_view,name = "top3_view"),
    path("log_in",views.log_in,name = "log_in"),
    path("check",views.check,name = "check"),
    path("log_out",views.log_out,name = "log_out"),
    path("fb_only",views.fb_only,name = "fb_only"),
    path("cros_api",views.cros_api,name = "cros_api"),
    path("line_only",views.line_only,name = "line_only"),
]