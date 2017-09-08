from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse
import re
from django.shortcuts import redirect
from .forms import UserForm
from django.db.models import Q
from django.contrib.auth.models import Permission, User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Equipments,EquipmentStatus
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    return render(request,'frontend/index.html', {'home' : True})
def items(request):
    all_items=Equipments.objects.all()
    template=loader.get_template('frontend/items.html')
    context={
        'items' : True,
        'all_items':all_items
    }
    return HttpResponse(template.render(context,request))
def detail(request,item_id):
    item=get_object_or_404(Equipments,pk=item_id)
    return render(request,'frontend/detail.html',{'item':item,
                                                  'remaining':item.quantity-item.TotalTaken})

def search(request):
        name = Equipments.objects.all()
        query = request.GET.get("q")
        name = name.filter(
            Q(name__icontains=query)
        ).distinct()
        return render(request, 'frontend/items.html', {
            'all_items':name
        })

def req(request,item_id):
    if not request.user.is_authenticated:
        return render(request, 'frontend/index.html', {'error_msg':'please log in'})
    else:
        equipment = get_object_or_404(Equipments, pk=item_id)
        if equipment.quantity < equipment.TotalTaken + int(request.POST['number']):
            return render(request, 'frontend/request.html', {'equipment': equipment,})
        else:
            equipment.TotalTaken += int(request.POST['number'])
            equipment.save()
            sub = 'New equipment desired by user '
            Msg = "%s desires %s : " % (
                request.user.username,
                equipment.name
            )
            frmemail = settings.EMAIL_HOST_USER
            toemail = str(equipment.MentorEmail)
            send_mail(sub, Msg, frmemail, [toemail], fail_silently=False)
            stay = EquipmentStatus()
            stay.Status = 1
            stay.Reason = request.POST['reason']
            stay.UserId = request.user
            stay.name = equipment
            stay.save()
            return render(request, 'frontend/request.html', {'equipment': equipment,
                                                             'remaining': equipment.quantity-equipment.TotalTaken})


class UserFormView(View):
    form_class = UserForm
    template_name = 'frontend/user_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                return render(request, self.template_name, {'form': form})
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('frontend:index')
        return render(request, self.template_name, {'form': form})


def update(request):
    user = request.user
    user.username = request.POST['username']
    user.email = request.POST['email']
    password = request.POST['password']
    if password is not None:
        user.set_password(password)
    user.save()
    return redirect('frontend:index')


def signin(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        if user.is_active:
            login(request, user)
    return redirect('frontend:index')


def logout_user(request):
    logout(request)
    return redirect('frontend:index')


def status(request):
    return render(request, 'frontend/orderstatus.html', {'track':request.user.equipmentstatus_set.all()})
