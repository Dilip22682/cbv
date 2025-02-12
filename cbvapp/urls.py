from django.urls import path
# from cbvapp.views import AllCompany,CompanyDetails
from cbvapp import views
from cbvapp import forms

urlpatterns=[
    path("",views.AllCompany.as_view(),name='list'),
    path("index/",views.html_page.as_view(),name='index'),
    path("create/",views.AddCompany.as_view(),name='create'),
    path("<int:pk>/",views.CompanyDetails.as_view(),name='detail'),
    path("edit/<int:pk>/",views.UpdateCompany.as_view(),name='edit'),
    path("delete/<int:pk>/",views.DelCompany.as_view(),name='delete'),
    path('emi/<int:id>',views.displayEmi,name='emi'),
    
]