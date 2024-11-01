from django.urls import path

from apteks import views

app_name = 'apteks'

urlpatterns = [
    path('apteks/', views.apteks, name='apteks'),
]