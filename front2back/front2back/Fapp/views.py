from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee

def djangoformview(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            i= form.cleaned_data['eid']
            n= form.cleaned_data['ename']
            s = form.cleaned_data['esal']
            e = form.cleaned_data['eexp']
            emp = Employee(eid=i,ename=n, esal=s, eexp=e)
            emp.save()
            return HttpResponse(f'Data Inserted- {i}, {n}, {s}, {e}')
        else:
            return HttpResponse("<h3> Invalid Forms </h3>")

    form = EmployeeForm()
    template_name='Fapp/djangoform.html'
    context = {'form': form}
    return render(request,template_name,context)


