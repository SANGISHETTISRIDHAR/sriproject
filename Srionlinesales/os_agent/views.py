import random

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DeleteView

from .models import Agent,Property,Blockproperty,Soldproperty
from Srionlinesales import sendsms


def agentlogincheck(request):
    if request.method == "POST":
        agntuname = request.POST.get("a1")
        agntpwd = request.POST.get("a2")
        try:
            result = Agent.objects.get(agent_un=agntuname,agent_pwd=agntpwd)
            otp = random.randint(10000,99999)
            result.otp=otp
            result.save()
            message="Hello Agent, This is your One Time Password:" + str(otp)
            # d1=sendsms.sendACASMS(agntcno, message)
            # import json
            # dd = json.loads(d1)
            # if dd["return"]:
            if True:
                request.session["username"]=agntuname
                return render(request, "os_agent_templates/os_agent_otp.html")
            else:
                return render(request,'os_agent_templates/os_agent_home.html')

        except:
            messages.error(request, "Invalid user")
            return render(request, "os_agent_templates/os_agent_home.html")
    else:
        return render(request,'os_agent_templates/os_agent_home.html')


def agentotpcheck(request):
    if request.method=="POST":
        otp=request.POST.get("agent_otp")
        try:
            result=Agent.objects.get(otp=otp)
            request.session["status"]=True
            return render(request,'os_agent_templates/os_agent_welcome.html')
        except:
            return render(request,'os_agent_templates/os_agent_home.html')
    else:
         return render(request,'os_agent_templates/os_agent_home.html')


def agentpropertysave(request):
    if request.method=="POST":
        name=request.POST.get("p2")
        location=request.POST.get("p3")
        size=request.POST.get("p4")
        price=request.POST.get("p5")
        facing=request.POST.get("p6")
        comments=request.POST.get("p7")
        photo=request.FILES["p8"]
        status="post"
        agentid=request.session["username"]
        Property(name=name,location=location,size=size,price=price,facing=facing,comment=comments,photo=photo,status=status,agent_id=agentid).save()
        qs=Property.objects.filter(agent_id=agentid)
        return render(request, 'os_agent_templates/os_agent_property.html',{"data":qs})


def agentproperty(request):
    agent=request.session['username']
    qs=Property.objects.filter(agent_id=agent,status='post')
    return render(request,'os_agent_templates/os_agent_property.html',{"data":qs})


def agenthome(request):
    request.session['status']=False
    return render(request,'os_agent_templates/os_agent_home.html')


def blockproperty(request):
    uname = request.session['username']
    qs = Property.objects.filter(agent_id=uname,status='post')
    list = []
    for x in qs:
        list.append(Blockproperty.objects.filter(property_no_id=x.no))
    return render(request, 'os_agent_templates/os_agent_blocked.html',{"data":list})


def soldproperty(request):
    pno = request.GET.get("no")
    cun = request.GET.get("cun")
    print(pno,cun)
    sd=Soldproperty(client_no_id=cun,property_no_id=pno).save()
    print(sd)
    sf=Property.objects.filter(no=pno).update(status="sold")
    print(sf)
    return render(request,'os_agent_templates/os_agent_sold_property.html')


def viewsoldproperty(request):
    agent = request.session['username']
    qs = Property.objects.filter(agent_id=agent,status="sold")
    return render(request,'os_agent_templates/os_agent_sold_property.html',{"data":qs})




class agentdeleteconformation(DeleteView):
    model = Property
    template_name ='os_agent_templates/os_agent_deleteconformation.html'
    success_url = '/osagent/agentproperty/'