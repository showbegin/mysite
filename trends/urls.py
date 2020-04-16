from django.urls import path

from . import views

app_name= 'trends'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:date_id>/', views.date, name='date'),
    path('<int:date>/<str:region>/', views.region, name='region')
]