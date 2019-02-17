from django.shortcuts import render,HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("Hello World")

def product(request):
    return render(request,'product_list.html') 

def product_view(request):
    return render(request,'product_view.html')   