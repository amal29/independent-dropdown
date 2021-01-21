from django.urls import include, path

from . import views

urlpatterns = [
    path('userlist', views.UserListView.as_view(), name='userlist'),
    path('', views.UserCreateView.as_view(), name='user_add'),
    path('ajax_load_service', views.load_services, name='ajax_load_service'),
    path('ajax_load_doctor', views.load_doctor, name='ajax_load_doctor'),

   ]