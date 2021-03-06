from django.urls import path
from . import views

app_name = 'coreapp'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('add',views.AddView.as_view(),name='add'),
    path('comics/', views.PostView.as_view(),name='comics'),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]