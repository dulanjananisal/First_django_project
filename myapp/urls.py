from django.urls import path
from .views import HomePageView, FormPageView, DetailPageView

app_name = 'myapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('forms/', FormPageView.as_view(), name='form'),
    path('details/<int:pk>', DetailPageView.as_view(), name='details'),
]