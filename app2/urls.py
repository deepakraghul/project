from app2 import views
from django.urls import path

urlpatterns = [

path('market/',views.market,name='market'),

]
