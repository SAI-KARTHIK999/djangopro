
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.biodata_form , name = "form"),
    path('/result', views.biodata_result , name ="result"),
]
