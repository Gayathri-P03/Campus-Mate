from django import forms

class StudentLoginForm(forms.Form):
    name = forms.CharField(max_length=100, label="Student Name")
    reg_no = forms.CharField(max_length=20, label="Registration Number")