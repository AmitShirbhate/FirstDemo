from django import forms

class EmployeeForm(forms.Form):
    eid = forms.IntegerField()
    ename = forms.CharField(max_length=32)
    esal = forms.FloatField()
    eexp = forms.FloatField()