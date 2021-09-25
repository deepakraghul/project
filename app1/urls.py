from app1 import views
from django.urls import path

urlpatterns = [

path('shopf/',views.shopf,name='shopf'),
path('done/',views.done,name='done')


]
