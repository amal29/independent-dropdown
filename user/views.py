from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import *
from .forms import Userprofileform
from django.shortcuts import render

class UserListView(ListView):
    model = Userprofile
    form_class = Userprofileform
    # context_object_name = 'students'

class UserCreateView(CreateView):
    model = Userprofile
    form_class = Userprofileform
    template_name = "userprofile_form.html"
    success_url="/"

def load_services(request):
    form=Userprofileform()
    print(form)

    category_id = request.GET.get('category')
    services = Service.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'service_dropdown_list_options.html', {'services': services})




def load_doctor(request):
    service_id = request.GET.get('service')
    print(service_id)
    doctors = Doctor.objects.filter(service_id=service_id).order_by('name')
    return render(request, 'doctor_dropdown_list_options.html', {'doctors': doctors})
