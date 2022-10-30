from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import LongToShort

# Create your views here.
def hello_world(request):
    return HttpResponse("Helllo how are you!!")

def task(request):
    context={"year":"2023","attendees":["Adi","Rishabh","Nikesh","sarthak"]}

    return render(request,"task.html",context)

def home_page(request):
    context={
        "submitted": False,
        "error": False
    }
    print(request.META)
    if request.method=="POST":
        #print(request.POST)
        data=request.POST
        
        longurl=data['longurl']
        customname=data['custom_name']

        try:
            context["long_url"]=longurl
            context["custom_name"]=request.build_absolute_uri()  + customname
            customname=request.build_absolute_uri()  + customname
            obj=LongToShort(long_url=longurl,custom_name=customname)
            obj.save()
            context["submitted"]=True
            context["date"]=obj.created_date
            context["clicks"]=obj.visit_count
            #print(long_url,custom_name)
        except:
            context["error"]=True
            
    else:
        print("USer didnkt submit yet")
    return render(request,"index.html",context)



def redirect_url(request,customname):
    row=LongToShort.objects.filter(custom_name=customname)
    print(row)
    if len(row)==0:
        return HttpResponse("This endpoint dosen't exist Error!!")
    obj=row[0]
    long_url=obj.long_url
    obj.visit_count+=1
    obj.save()
    return redirect(long_url)


def analytics(request):
    rows=LongToShort.objects.all()
    context={
        "rows":rows
    }
    return render(request,"analytics.html",context)

