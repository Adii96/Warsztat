
"""Warsztat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Warsztatapp.views import AddRoom, RoomList, Index, \
    DeleteRoom, ModifyRoom, ReserveViev, DetailsRoom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('room/new/', AddRoom.as_view()),
    path('room-list/', RoomList.as_view(), name='room-list'),
    #path('', RoomList.as_view(), name='room-list'),
    path('room/delete/<int:id>/room-list', DeleteRoom.as_view()),
    path('room/modify/<int:id>/', ModifyRoom.as_view()),
    path('room/reserve/<int:id>/', ReserveViev.as_view()),
    path('room/details/<int:id>/', DetailsRoom.as_view()),

]
