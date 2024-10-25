from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("upload/", views.upload_file, name="upload_file"),
    path("", RedirectView.as_view(url='/upload/', permanent=True))
]
