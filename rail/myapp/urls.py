from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('live/',views.live,name="live"),


]
