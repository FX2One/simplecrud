from django.urls import path
from . import views

app_name = 'coreapp'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.SingleView.as_view(), name='single')
]