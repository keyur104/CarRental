import os
import sys
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
import mysql.connector
from _overlapped import NULL
from django.template.context_processors import request
import pandas as pd
from django.http import HttpResponse
import http.client
import traceback
#from scrapy.http import HtmlResponse
import time
import random as r
import smtplib
from datetime import datetime
from dateutil.parser import parse
#from .models import result
from datetime import date
from _ast import And
import matplotlib.pyplot as plt

PICKLOC=""
DROPLOC=""
PICKDATE=date.today()
DROPDATE=date.today()
PICKTIME=""
reslt=""
FULLNAME=""
ADDRESS=""
CONTACTNO=0
EMAIL=""
TOTAL=0
CARNAME=""
reslt=""
otp=""
USEROTP=""
DAYS=0
PICKDATE1=date.today()
DROPDATE1=date.today()
CONTACT1=""


# Create your views here.
def index(request):
    return render(request,'index.html')

def userlogin(request):
    return render(request,'userlogin.html')

def afterlogin(request):
    try:
        USERNAME=request.GET['username']
    except:
        USERNAME=False
    try:
        PWD=request.GET['pass']
    except:
        PWD=False   
    
    print(USERNAME)
    print(PWD)
    if USERNAME=='admin' and PWD =='admin123' :
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
        mycursor=mydb.cursor()
        
        mycursor.execute("select * from carcust ")
        avl=mycursor.fetchall()
        
         
        return render(request,'afterlogin.html',{'all':avl}) 
    else:
        return render(request,'userlogin.html',{'msg':"invalid credentials"})       


def adminsearch(request):
    return render(request,'adminsearch.html')

def checkname(request):
    try:
        NAMESRCH=request.POST['namesrch']
        
    except:
        NAMESRCH=False
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
    mycursor=mydb.cursor()    
    
    mycursor.execute("select * from carcust where custName='{}'".format(NAMESRCH))
    nameres=mycursor.fetchall()
    
    return render(request,'adminsearch.html',{'nameres':nameres})
def checkmob(request):
    try:
        MOBSRCH=request.POST['mobsrch']
        
    except:
        MOBSRCH=False
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
    mycursor=mydb.cursor()    
    
    mycursor.execute("select * from carcust where contactNo='{}'".format(MOBSRCH))
    nameres=mycursor.fetchall()
    
    return render(request,'adminsearch.html',{'nameres':nameres})
def checkemail(request):
    try:
        EMAILSRCH=request.POST['emailsrch']
        
    except:
        EMAILSRCH=False
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
    mycursor=mydb.cursor()    
    
    mycursor.execute("select * from carcust where email='{}'".format(EMAILSRCH))
    nameres=mycursor.fetchall()
    
    return render(request,'adminsearch.html',{'nameres':nameres})

def backtomain(request):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
    mycursor=mydb.cursor()
        
    mycursor.execute("select * from carcust ")
    avl=mycursor.fetchall()
        
         
    return render(request,'afterlogin.html',{'all':avl})

def addrec(request):
    return render(request,'addrec.html')
def addfinal(request):
    try:
        NEWCAR=request.POST['newcar']
    except:
        NEWCAR=False
    try:
        NEWKM=request.POST['newkm']
    except:
        NEWKM=False
    try:
        NEWDAY=request.POST['newday']
    except:
        NEWDAY=False      
    
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
    mycursor=mydb.cursor()
        
    
    #mycursor.execute("insert into cdtls values('{}','{}','{}')".format(NEWCAR,NEWDAY,NEWKM))
    mycursor.execute("INSERT INTO cdtls (`Cname`, `pickLoc`, `dropLoc`, `pickDate`, `dropDate`, `pickTime`, `RateD`, `Ratekm`, `status`,`counter`) VALUES ('{}', 'city', 'city', '2019-10-10', '2019-10-10', '1:00am', '{}', '{}', 'available','0')".format(NEWCAR,NEWDAY,NEWKM))
    mydb.commit()
    
    
    return render(request,'addrec.html',{'ins':"data inserted successfully"})

def analdata(request):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
    mycursor=mydb.cursor()
    
    mycursor.execute("select Cname from cdtls ")
    cnames=mycursor.fetchall()
    
    mycursor.execute("select counter from cdtls ")
    ccount=mycursor.fetchall()
    
    plt.title('Analyzing data by Car Count')
    
    labels =cnames
    ''' 
    sizes = []
    sizes.append(ree1)
    sizes.append(ree2)
    sizes.append(ree3)
    sizes.append(ree4)
    sizes.append(ree5)
    sizes.append(ree6)
    sizes.append(ree7)
    sizes.append(ree8)
    sizes.append(ree9)
    sizes.append(ree10)
    '''
    
    #colors = ['gold', 'yellowgreen', 'lightcoral','lime','blue','yellow','Aqua','Navy','Green','Orange']
    
    
    plt.pie(ccount,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.legend(labels,loc=0)

    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    return render(request,"analdata.html")
def CustInfo(request):
    global PICKLOC
    global DROPLOC
    global PICKDATE
    global DROPDATE
    global PICKTIME
    global reslt
    global DAYS
    try:
        PICKLOC=request.POST['pickLoc']
        
    except:
        PICKLOC=False
    try:        
        DROPLOC=request.POST['dropLoc']
    except:
        DROPLOC=False
    try:    
        PICKDATE=request.POST['pickDate']
        PICKDATE1=datetime.date(datetime.strptime(PICKDATE, '%m/%d/%Y'))
    except:
        PICKDATE=False    
    try:
        DROPDATE=request.POST['dropDate']
        DROPDATE1=datetime.date(datetime.strptime(DROPDATE, '%m/%d/%Y'))
    except:
        DROPDATE=False
    
    try:
        PICKTIME=request.POST['pickTime']
    except:
        PICKTIME=False
    
    
    print(PICKLOC)
    print(DROPLOC)
    print(PICKDATE1)
    print(DROPDATE1)
    print(PICKTIME)
    
    if PICKLOC=="" or DROPLOC=="" or PICKDATE=="" or DROPDATE=="" or PICKTIME=="" or PICKDATE1 < date.today() or DROPDATE1 < date.today():
        return render(request,'index.html',{'warn1':"please fill all fields Properly"})
    else:
        DAYS=(DROPDATE1-PICKDATE1).days + 1
        print(DAYS)
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
        mycursor=mydb.cursor()
    
   # mycursor.execute("insert into cdtls values('%s','%s','%s','%y%m%d','%y%m%d','%H:%M','%s','%s');",('scorpio',PICKLOC,DROPLOC,PICKDATE,DROPDATE,PICKTIME,'2200','10'))
    #mycursor.execute("insert into cdtls values('{}','{}','{}','{}','{}','{}','{}','{}','{}');".format('scorpio',PICKLOC,DROPLOC,PICKDATE,DROPDATE,PICKTIME,'2200','10',NULL))
    #print("insert into cdtls values('{}','{}','{}','{}','{}','{}','{}','{}','{}');".format('scorpio',PICKLOC,DROPLOC,PICKDATE,DROPDATE,PICKTIME,'2200','10',NULL))
    #mycursor.execute("select Img,Cname,RateD,Ratekm from cdtls where '{}' and '{}' not  between pickDate and dropDate ".format(PICKDATE,DROPDATE))
        mycursor.execute("update cdtls set status='{}' where dropDate < '{}'".format("available",date.today()))
        mydb.commit()
        mycursor.execute("select Img,Cname,RateD,Ratekm from cdtls where status='{}'".format('available'))
    
    #result="select Cname from cdtls where '{}' and '{}' not  between PickupDate and DropoffDate ;".format(PICKDATE,DROPDATE)
        reslt=list(mycursor.fetchall())
        return render(request,'CustInfo.html')



def search(request):
    global otp
    try:
        USEROTP=request.POST['auth']
        
    except:
        USEROTP=False
    
    
    
    
    
    if otp==USEROTP:
        
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
        mycursor=mydb.cursor()
        mycursor.execute("insert into custinforrmation values('{}','{}','{}','{}')".format(FULLNAME,ADDRESS,CONTACTNO,EMAIL))
        mydb.commit()
        mycursor.close()
        return render(request,'search.html',{'Result':reslt})
        otp=""
    else:
        return render(request,'authentication.html',{'msg1':"Invalid OTP"})
    
     
       
    #except:
    
        
   # mycursor.execute("INSERT INTO cdetails(Cname, PickupLoc, DropLOc, PickupDate, DropoffDate, PickupTime, RateD, Ratekm) VALUES ('%s','%s','%s','%s','%s','%d','%s','%s')",('hello',PICKLOC,DROPLOC,PICKDATE,DROPDATE,PICKTIME,2500,12))
  #  sl="insert into cdetails values (%s,%s,%s,%d %m %y,%d %m %y,%H:%i %p,%s,%s)"
    #print(sl,('hello',PICKLOC,DROPLOC,PICKDATE,DROPDATE,PICKTIME,'2500','12'))
   # mycursor.execute(sl,('hello',PICKLOC,DROPLOC,PICKDATE,DROPDATE,PICKTIME,'2500','12'))
    '''try:
        query="select Cname from cdetails where '%y%m%d' and '%y%m%d'  between PickupDate and DropoffDate ;"
        value=(PICKDATE,DROPDATE)
        mycursor.execute(query,value)
        result=mycursor.fetchall()
        mycursor.close()
        return render(request,'search.html',{'result':res})
    except:
        print("Connection failed")        
    '''
def authentication(request):
    global FULLNAME
    global ADDRESS
    global CONTACTNO
    global EMAIL
    global CONTACT1
    
    
 
    #print(res)
    #res=result.objects.all()   
    #print(reslt)
    #return (reslt)
    try:
        FULLNAME=request.POST['fullname']
        
    except:
        FULLNAME=False
    try:        
        ADDRESS=request.POST['address']
    except:
        ADDRESS=False
    try:    
        CONTACTNO=request.POST['contact']
        CONTACT1=str(request.POST['contact'])
    except:
        CONTACTNO=False    
    try:
        EMAIL=request.POST['email']
    except:
        EMAIL=False

    
    s=smtplib.SMTP('smtp.gmail.com',587)
    
    s.ehlo()
    
    s.starttls()
    
    #s.ehlo()
    global otp
   
    
    
    
    if FULLNAME=="" or ADDRESS=="" or CONTACTNO=="" or EMAIL=="" or len(CONTACT1)!=10:
        return render(request,'CustInfo.html',{'warn':"please fill all fields Properly"})
    else:
        for i in range(4):
            otp+=str(r.randint(1,9))
        print ("Your One Time Password is ")
        print (otp)
        s.login('boiii2412@gmail.com','motorcop')
    
        subject = 'Autoroad -Authentication '
        body = 'OTP For your Ongoing booking with Autoroad is:',otp
    
        message = f'Subject : {subject}\n\n {body}'
    
        s.sendmail('boiii2412@gmail.com',EMAIL,message)
    
        print ('HEY AN EMAIL HAS BEEN SENT!')
    
        s.quit()
        return render(request,'authentication.html')



def rent(request):
    #print(search(request))
    #print('result',res)
    return render(request,'rent.html')
    

def rentd(request):
    return render(request,'rentd.html',{'tdays':DAYS})

def procdkms(request):
    
    return render(request,'procdkms.html')

def procdday(request):
    
    return render(request,'procdday.html')
def booked(request):
    global PICKTIME
    global TOTAL
    global CARNAME
    global PICKLOC
    global DROPLOC
    global CONTACTNO
    global EMAIL
    global FULLNAME
    global PICKDATE1
    global DROPDATE1
   
    
    print("inside py")
    time.sleep(1)
    f=open("C:\\Users\\keyur\\Downloads\\data.txt","r")
    contents=f.readlines()
    TOTAL=contents[0]
    CARNAME=contents[1]
    print(contents[0])
    print(contents[1])
    f.close()
    os.remove("C:\\Users\\keyur\\Downloads\\data.txt")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="carrental")
    mycursor=mydb.cursor()
    print(PICKTIME)
    mycursor.execute("update cdtls set counter=counter + 1 where Cname='{}'".format(CARNAME))
    mydb.commit()
    mycursor.execute("insert into carcust values('{}','{}','{}','{}','{}','{}','{}')".format(CONTACTNO,FULLNAME,EMAIL,CARNAME,PICKLOC,DROPLOC,TOTAL))
    mydb.commit()
    mycursor.execute("update cdtls set status='{}',pickDate='{}',dropDate='{}',pickTime='{}' where Cname='{}'".format('Booked',PICKDATE1,DROPDATE1,PICKTIME,CARNAME))
    mydb.commit()
    mycursor.close()
    
    s=smtplib.SMTP('smtp.gmail.com',587)
    
    s.ehlo()
    
    s.starttls()
    
    s.login('boiii2412@gmail.com','motorcop')
    
    subject = 'Autoroad - Booking Confirmation '
    body = 'HEY',FULLNAME,'!!,You have booked a', CARNAME ,'from ',PICKDATE,'to',DROPDATE,',.This is to inform you that your booking is CONFIRMED' 
    
    message = f'Subject : {subject}\n\n {body}'
    
    s.sendmail('boiii2412@gmail.com',EMAIL,message)
    
    print ('HEY AN EMAIL HAS BEEN SENT!')
    
    s.quit()
    
    
    
  
    
    return render(request,'booked.html')