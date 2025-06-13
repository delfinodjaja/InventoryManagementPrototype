from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import UserRegisterForm,PatientLogForm
from .models import inventoryItem,patient_log
from django.contrib import messages
from django.utils.timezone import localtime
from django.http import HttpResponseForbidden
from django.core.serializers.json import DjangoJSONEncoder
import json


# Create your views here.
class Index(TemplateView):
    template_name='inventory/index.html'

class SignUpView(View):
    def get(self,request):
        form=UserRegisterForm()
        return render(request,'inventory/signup.html',{'form':form})
    def post(self,request):
        form=UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request,user)
            return redirect('index')
        return render(request, 'inventory/signup.html', {'form': form})

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='Doctor').exists()

    def handle_no_permission(self):
        return HttpResponseForbidden("You are not allowed to access this page.")

    def get(self, request):
        items = inventoryItem.objects.all()

        patient_ = patient_log.objects.filter(doctor=self.request.user)
        appointments=[]
        for p in patient_:
            appointments.append({
                'date': localtime(p.date).strftime('%b %d, %Y %I:%M %p'),
                'name': p.name,
                'category': str(p.category) if p.category else 'N/A',
        })
        total_quantity = sum(i.quantity for i in items)
        low_stock = sum(1 for i in items if i.quantity < 10)
        return render(request, 'inventory/dashboard.html', {
            'total': total_quantity,
            'low_stock': low_stock,
            'patient':json.dumps(appointments, cls=DjangoJSONEncoder),
        })

class inventory(View):
    def get(self, request):
        #items=inventoryItem.objects.filter(user=self.request.user.id).order_by('id')
        items = inventoryItem.objects.all()
        return render(request,'inventory/inventory_page.html',{'items':items})

class create_appointment(LoginRequiredMixin,View):
    def get(self, request):
        form = PatientLogForm()
        return render(request, 'inventory/appointment.html', {'form': form})

    def post(self, request):
        form = PatientLogForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = request.user.username

            conflict = patient_log.objects.filter(doctor=appointment.doctor, date=appointment.date).exists()
            if conflict:
                messages.error(request, "You already have an appointment at this time.")
                return render(request, 'inventory/appointment.html', {'form': form})

            appointment.save()
            messages.success(request, "Appointment created successfully.")
            return redirect('index')

        return render(request, 'inventory/appointment.html', {'form': form})