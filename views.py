from django.shortcuts import render, redirect
from .forms import Employeeform
from .models import employee
# Create your views here.
def employee_list(request):
    x =employee.objects.all()              # here employee is model.py
    return render(request,"employee_list.html",{'emp':x})

def employee_form(request,id=0):
    if request.method=="GET":
        if id==0:
            a=Employeeform()                 # here Employeeform is in form.py
        else:
            emp=employee.objects.get(pk=id)
            a=Employeeform(instance=emp)
        return render(request,"employee_form.html",{"form":a})
    else:
        if id==0:
            a=Employeeform(request.POST)
        else:
            emp=employee.objects.get(pk=id)
            a=Employeeform(request.POST,instance=emp)

        if a.is_valid():
            a.save()
        return redirect("/list")

def employee_delete(request,id):
    emp=employee.objects.get(pk=id)
    emp.delete()
    return redirect('/list')
