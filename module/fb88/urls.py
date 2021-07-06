from django.urls import path
from .views import Fb88ListView


urlpatterns = [
    path('fb88', Fb88ListView.as_view(),name='list_fb88'),
]