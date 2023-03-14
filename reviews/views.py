from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = request.GET.get("name") or "world" # if name is None, use "world"
    return HttpResponse(f"Hello, {name}. You're at the reviews index.")