from django.template import loader
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Student
from .forms import Add_student
import datetime
from django.db.models import Q
from django.views.decorators.http import require_http_methods

# Create your views here.


def home(request):
    st = Student.objects.all().order_by('id').values()
    a = datetime.datetime.now()
    context = {'st' : st, 'a':a}
    # return render(request, 'enroll/home.html', context)
    template = loader.get_template('enroll/home.html')
    return HttpResponse(template.render(context))


def add_student(request):
    if request.method== 'POST':
        fm = Add_student(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = Add_student()
    return render(request, 'enroll/add_student.html', {'fm':fm})



def update_data(request, id):
    if request.method=="POST":
        pi = Student.objects.get(pk=id)
        fm = Add_student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm=Add_student(instance=pi)
    return render(request, 'enroll/update_data.html', {'id':id, 'fm':fm})



def delete_data(request, id):
    if request.method=="POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('')



def members(request):
  mymembers = Employee.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))