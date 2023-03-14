from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    name = request.GET.get("name") or "world" # if name is None, use "world"
    
    return render(request, "base.html", {"name": name})