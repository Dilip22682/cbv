
from django import forms
from django.forms import ModelForm
from cbvapp.models import RentBooking



    
   
# code

class Form_RentBooking(forms.ModelForm):
    class Meta:
        model=RentBooking
        fields='__all__'

# class EmiCalform(forms.ModelForm):
    # total__loan_amt=forms.IntegerField()
    # months_of_repayment=forms.IntegerField()
    # rate_of_intrest=forms.FloatField()
    
    # amount = forms.IntegerField(label="Loan Amount")
    # rate = forms.FloatField(label="Interest Rate")
    # tenure = forms.IntegerField(label="Tenure (in months)")
    
# class EmiForm(forms.Form):
#     principal = forms.DecimalField(label="Principal Amount", max_digits=10, decimal_places=2)
#     rate = forms.DecimalField(label="Intrest Rate  (%)", max_digits=5, decimal_places=2)
#     months= forms.IntegerField(label="Time (in months)")
        
    