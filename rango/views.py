from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world! Go to the <a href='/rango/about/'>about</a> page.")

def about(request):
    return HttpResponse("Rango Says: Here is the about page. Go back to the <a href='/rango/'>index</a> page.")