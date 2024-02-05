from django.urls import path
from .views import home, add_show, addsht, delete_rec, update_rec

urlpatterns = [
    path('',home, name='home'),
    path('add-show/', add_show, name='addshow'),
    path('add-show/', addsht, name='addsht'),
    path('delete/<int:id>',delete_rec, name='deleterec'),
    path('update/<int:id>', update_rec, name='updaterec')
]
