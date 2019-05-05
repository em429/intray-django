from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'intray'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add/', views.add, name='add'),
    path('process/', views.process, name='process'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    path('archived_item/<uuid:slug>/',
         views.ArchivedItemView.as_view(),
         name='archived_item'
    ),
]
