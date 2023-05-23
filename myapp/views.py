from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .forms import form
from .models import Asset
# Create your views here.




def upload(request):
    if request.method=="POST":
        Form=form(request.POST)
        if Form.is_valid():
            try:
                Form.save()
                return redirect("/")
            except:
                pass
    else:
        Form=form()
    info=Asset.objects.all()
    
    fe=[]
    me=[]
    for i in info:
        if i.category=="Workstation":
            fe.append(i)
        elif i.category=="Server":
            me.append(i)
    f=len(fe)
    m=len(me)
    re=[]
    de=[]
    pe=[]
    lo=[]
    for i in info:
        if i.status=="Ready to deploy":
            re.append(i)
        elif i.status=="Deployed":
            de.append(i)
        elif i.status=="Pending":
            pe.append(i)
        elif i.status=="Lost":
            lo.append(i)
    r=len(re)
    d=len(de)
    p=len(pe)
    l=len(lo)

    return render(request,'upload_form.html',{'form':Form,'info':info,'f':f,'m':m,'r':r,'d':d,'p':p,'l':l})

def edit(request, id):
    info =Asset.objects.get(id=id)
    return render(request,'edit.html',{'info':info})
def update(request, id):
    info =Asset.objects.get(id=id)
    Form =form(request.POST, instance=info)
    if Form.is_valid():  
        Form.save()
        return redirect('/')
    return render(request,'edit.html',{'info':info})  


def destroy(request,id):
    try:
        sel = Asset.objects.get(id = id)
    except Asset.DoesNotExist:
        return redirect('/')
    sel.delete()
    return redirect('/')

