from django.shortcuts import render

# Create your views here.
def showBucket(request):
    return render(request,"Bucket.html",{"title":"Bucket","path":"css/MainPage/style.css"})