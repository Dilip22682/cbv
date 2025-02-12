from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse 
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from cbvapp.models import Company,Products
from django.urls import reverse_lazy
# from cbvapp.forms import EmiCalform
# from .forms import EmiForm

# Create your views here

class html_page(TemplateView):
    template_name="index.html"
    
class AllCompany(ListView):
    model=Company
    
class CompanyDetails(DetailView):
    model=Company
    context_object_name="company_info"
 
class AddCompany(CreateView):
    model=Company
    fields='__all__'    
    
class UpdateCompany(UpdateView):
    model=Company
    fields=['name','CEO']

class DelCompany(DeleteView):
    model=Company
    success_url=reverse_lazy('list')
    
    
# this for emi from
# class DisplayEmiView(FormView):
#     template_name = 'emi_form.html'  # Specify the template to render the form
#     form_class = EmiForm  # Link the form class
#     context_object_name="product_info"
    
#     def form_valid(self, form):
#         # Get cleaned data from the form
#         principal = form.cleaned_data['principal']
#         rate = form.cleaned_data['rate']
#         months = form.cleaned_data['months']
        
#         print(principal = form.cleaned_data['principal'])
#         print(rate = form.cleaned_data['rate'])
#         print(months = form.cleaned_data['months'])
        
#         monthly_rate = rate / (12 * 100)
#         emi1 = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        
#         return self.render_to_response(self.get_context_data(emi1=round(emi1, 2)))

    

def displayEmi(request,id):
    product_data=Products.objects.get(id=id)
    print(product_data.price)
    
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        tensure = int(request.POST['months'])
        interest = int(request.POST['rate'])
        # loan_exceeded=amount<product_data.price
        if amount<product_data.price:
            # print("loan exceeded:",loan_exceeded)
            r = interest / (interest * 100)
            numerator = amount * r * (1+r) ** tensure
            denominator = (1+r) ** tensure - 1
            emi_per_month =  numerator / denominator
            # loan_exceeded=
            return render(request, 'emi_form.html',{'emi_per_month':emi_per_month})
        else:
            return render(request,'emi_form.html',{'error':"<h1>Loan should not be greater than {{form.price}} </h1>"})         
          
    
    return render(request, 'emi_form.html',{'form':product_data})
   
    