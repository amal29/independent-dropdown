from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.UserListView.as_view(), name='userlist'),
    path('', views.UserCreateView.as_view(), name='user_add'),
    # path('<int:pk>/', views.StudentUpdateView.as_view(), name='student_change'),
    path('ajax_load_service', views.load_services, name='ajax_load_service'),
    path('ajax_load_doctor', views.load_doctor, name='ajax_load_doctor'),

   ]