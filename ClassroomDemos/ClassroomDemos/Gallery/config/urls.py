from django.views.generic import RedirectView
from django.urls import path
from django.contrib import admin

from photos.views import PhotoDetailView, PhotoListView


urlpatterns = [
    path("admin/", admin.site.urls),

    # Home
    path('', RedirectView.as_view(url='photo/')),

    # Photos
    path('photo/', PhotoListView.as_view()),
    path('photo/<int:id>', PhotoDetailView.as_view()),
]
