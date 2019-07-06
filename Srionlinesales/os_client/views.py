import random

from django.shortcuts import render
from .models import Client,Complaint
from django.contrib import messages
from os_agent.models import Property,Blockproperty
# Create your views here.
def clientlogincheck(request):
    if request.method== "POST":
        cuname=request.POST.get("c1")
        cpwd=request.POST.get("c2")
        try:
            result=Client.objects.get(client_un=cuname,client_pwd=cpwd)
            otp=random.randint(10000,99999)
            result.otp=otp
            result.save()
            if True:
                request.session['username']=cuname
                qs=Client.objects.all()
                return render(request,"os_client_templates/os_client_otp.html",{"data":qs})
            else:
                messages.info(request,"sorry unable to send otp")
                return render(request,"os_client_templates/os_client_home.html")
        except:
            messages.success(request,"Invalid user")
            return render(request,"os_client_templates/os_client_home.html")
    else:
        return render(request,"os_client_templates/os_client_home.html")


def clientregister(request):
    return render(request,'os_client_templates/os_client_registration.html')


def clientsavedata(request):
    if request.method=="POST":
        name=request.POST.get("c1")
        uname=request.POST.get("c2")
        upwd=request.POST.get("c3")
        contactno=request.POST.get("c4")
        addrs=request.POST.get("c5")
        photo=request.FILES["c6"]
        otp=12345
        Client(name=name,client_un=uname,client_pwd=upwd,contact_no=contactno,address=addrs,photo=photo,otp=otp).save()
        qs=Client.objects.all()
        messages.success(request,name+ "is Registerd")
        return render(request,"os_client_templates/os_client_home.html")
    else:
        messages.success(request,"Your Registration not Successfull")
        return render(request,"os_client_templates/os_client_registration.html")


def clientotpcheck(request):
    if request.method=="POST":
        otp=request.POST.get('client_otp')
        try:
            res=Client.objects.get(otp=otp)
            request.session['status']=True
            qs=Client.objects.all()
            return render(request,'os_client_templates/os_client_welcome.html',{"data":qs})
        except:
            messages.error(request,"Invalid OTP")
            return render(request,'os_client_templates/os_client_home.html')
    else:
        return render(request, "os_client_templates/os_client_home.html")


def clientproperty(request):
    qs=Property.objects.filter(status='post')
    return render(request,'os_client_templates/os_client_property.html',{"data":qs})


def blockproperty(request):
    uname=request.GET.get("uname")
    no=request.GET.get("no")
    print(uname,no)
    qs=Blockproperty.objects.filter(client_un_id=uname,property_no_id=no)
    if qs:
        messages.info(request,"Blocked Property")
        qs=Property.objects.all()
        return render(request,'os_client_templates/os_client_property.html',{"data":qs})
    else:
        Blockproperty(client_un_id=uname,property_no_id=no).save()
        ws=Blockproperty.objects.filter(client_un_id=uname)
        return render(request,"os_client_templates/os_client_bloked.html",{"data":ws})

def unblockproperty(request):
    uname=request.GET.get("uname")
    no=request.GET.get("no")
    Blockproperty.objects.filter(client_un_id=uname,property_no_id=no).delete()
    qs=Blockproperty.objects.filter(client_un_id=uname)
    return render(request,'os_client_templates/os_client_bloked.html',{"data":qs})


def blokedproperty(request):
    uname = request.session['username']
    ws = Blockproperty.objects.filter(client_un_id=uname)
    return render(request, 'os_client_templates/os_client_bloked.html',{"data":ws})


def complaint(request):
    return render(request,'os_client_templates/os_complaint.html')


def comsubmit(request):
    uname=request.session['username']
    comp=request.POST.get("c1")
    Complaint(client_un_id=uname,comment=comp).save()
    qs=Complaint.objects.all()
    return render(request,'os_client_templates/os_complaint.html',{"data":qs})


def comcdelete(request):
    no=request.GET.get("no")
    Complaint.objects.filter(no=no).delete()
    qs=Complaint.objects.all()
    return render(request,"os_client_templates/os_complaint.html",{"data":qs})