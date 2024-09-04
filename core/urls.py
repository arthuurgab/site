from django.contrib import admin
from django.urls import path, include
from home import urls as h

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(h)),
]
