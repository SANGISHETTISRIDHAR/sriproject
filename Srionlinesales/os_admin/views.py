from django.shortcuts import render
from os_agent.models import Property
from os_client.models import Client
from .models import Adminlogin,Agent
import random
from django.contrib import messages
from Srionlinesales import sendsms
from django.views.generic import DeleteView
from Srionlinesales import sendsms


def adminlogincheck(request):
    if request.method == "POST":
        ausername = request.POST.get("admin_username")
        apassword = request.POST.get("admin_password")

        try:
            result = Adminlogin.objects.get(contactno=ausername,password=apassword)
            otp = random.randint(10000,99999)
            result.otp=otp
            result.save()
            print(result)
            message="Hello Admin, This is your One Time Password:" + str(otp)
            d1=sendsms.sendACASMS(ausername, message)

            # import json
            # dd = json.loads(d1)
            # if dd["return"]:
            if d1:
                return render(request, "os_admin_templates/os_admin_otp.html")
            else:
                return render(request, "os_admin_templates/os_admin_login.html",{"error":"Sorry Unable to send OTP"})

        except:
            messages.error(request, "Invalid user")
            return render(request, "os_admin_templates/os_admin_login.html")

    else:
        return render(request, "os_admin_templates/os_admin_login.html")

def adminotpcheck(request):
    if request.method=="POST":
        otp=request.POST.get("admin_otp")
        try:
            result=Adminlogin.objects.get(otp=otp)
            request.session["status"]=True
            return render(request,"os_admin_templates/os_admin_welcome.html")
        except:
            return render(request,"os_admin_templates/os_admin_login.html")
    else:
        messages.error(request,"INVALID OTP No")
        return render(request,"os_admin_templates/os_admin_login.html")


def agentregister(request):
    qs=Agent.objects.all()
    return render(request, "os_admin_templates/os_admin_agentreg.html", {"data":qs})


def savedata(request):
    if request.method =="POST":
        no=request.POST.get("agentno")
        name=request.POST.get("agentname")
        addrs=request.POST.get("agentadrs")
        aun=request.POST.get("agentusername")
        apwd=request.POST.get("agentpassword")
        acno=request.POST.get("agentcontactno")
        photo=request.FILES["agentphoto"]
        otp=123456
        Agent(no=no,name=name,address=addrs,agent_un=aun,agent_pwd=apwd,contactno=acno,photo=photo,otp=otp).save()
        qs=Agent.objects.all()
        return render(request, "os_admin_templates/os_admin_agentreg.html", {"data":qs})
    else:
        return render(request, "os_admin_templates/os_admin_login.html")


def agentdelete(request):
        idno=request.GET.get("idno")
        Agent.objects.get(no=idno).delete()
        qs=Agent.objects.all()
        return render(request, "os_admin_templates/os_admin_welcome.html", {"data":qs})

def adminlogout(request):
    request.session["status"] = False
    return render(request,"os_admin_templates/os_admin_welcome.html")


def aboutsus(request):
    return render(request, "os_admin_templates/os_about_us.html")


def contactus(request):
    return render(request, "os_admin_templates/os_contactus.html")


def adminhome(request):
    return render(request,'os_admin_templates/os_admin_home.html')


def viewallclients(request):
    qs = Client.objects.all()
    return render(request, "os_admin_templates/os_client.html", {"data": qs})


def propertyall(request):
    qs = Property.objects.filter(status="post")
    return render(request, "os_admin_templates/propertyall.html", {"data": qs})


def deleteclient(request):
    uname=request.GET.get("idno")
    Client.objects.filter(client_un=uname).delete()
    qs=Client.objects.all()
    return render(request,'os_admin_templates/os_client.html',{"data":qs})