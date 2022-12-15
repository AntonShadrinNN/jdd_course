"""jdd_course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from cities.views import *

urlpatterns = [
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete_view'),
    path('', home, name='home'),
    path('<int:pk>/', HomeDetailView.as_view(), name='detail_home'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update_view'),
    path('create/', CityCreateView.as_view(), name='create_view'),
]


