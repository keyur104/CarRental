from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    #path('index',views.index,name='index'),
    path('CustInfo',views.CustInfo,name='CustInfo'),
    path('search',views.search,name='search'),
    path('rent',views.rent,name='rent'),
    path('rentd',views.rentd,name='rentd'),
    path('procdkms',views.procdkms,name='procdkms'),
    path('procdday',views.procdday,name='procdday'),
    path('booked',views.booked,name='booked'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('afterlogin',views.afterlogin,name='afterlogin'),
    path('authentication',views.authentication,name='authentication'),
    path('adminsearch',views.adminsearch,name='adminsearch'),
    path('checkname',views.checkname,name='checkname'),
    path('checkmob',views.checkmob,name='checkmob'),
    path('checkemail',views.checkemail,name='checkemail'),
    path('backtomain',views.backtomain,name='backtomain'),
    path('addrec',views.addrec,name='addrec'),
    path('addfinal',views.addfinal,name='addfinal'),
    path('analdata',views.analdata,name='analdata')
    

    ]