from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('buy/<int:id>/', buy, name='buy'),

]
