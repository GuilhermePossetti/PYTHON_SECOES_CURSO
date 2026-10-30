from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id/>', views.index, name='contact'),
]