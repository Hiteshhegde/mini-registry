
from django.urls import path, include
from .views import DomainnameView

urlpatterns = [
    path('', DomainnameView.as_view(), name='domainname-info'),
    

]