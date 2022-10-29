from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("Helllo how are you!!")

def task(request):
    context={"year":"2023","attendees":["Adi","Rishabh","Nikesh","sarthak"]}

    return render(request,"task.html",context)

def home_page(request):
    if request.method=="POST":
        print(request.POST)
    else:
        print("USer didnkt submit yet")
    return render(request,"index.html")
