from django import forms

class SigninForm(forms.Form):
    name = forms.CharField(label='نام و نام خانوادگی')
    phone = forms.CharField(label='تلفن',max_length=11)
    password=forms.CharField(label='رمز عبور',min_length=8)
    confirmPassword=forms.CharField(label='تکرار رمز عبور',min_length=8)