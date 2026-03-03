from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("dnd/", include("dnd.urls")),
    path('admin/', admin.site.urls),
]
