from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def employee_list(request):

    EmpList = Employee.objects.all() 

    return render(request,"employee_list.html",{'EmpList':EmpList})

def employee_form(request,id=0):
    if request.method =="GET": 
        if id==0:
          EmpForm = EmployeeForm()
        else:
          employee = Employee.objects.get(pk=id)
          EmpForm = EmployeeForm(instance=employee)

        return render(request,"employee_form.html",{'form':EmpForm})
    else:
        if id == 0:
           EmpForm = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            print(employee)
            print("Hello world")
            EmpForm = EmployeeForm(request.POST,instance= employee)

        if EmpForm.is_valid():
               EmpForm.save()
        

        return redirect('/employee/list')
 

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

