from django.urls import path
from .views import ProfileView 

app_name = 'account'

urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),

]
