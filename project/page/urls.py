from django.urls import path
#from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:pk>/', views.detail, name='detail'),
    #path('contact/', RedirectView.as_view(url='/page/1/'))
]
