from django.shortcuts import render, HttpResponse, redirect
#The index function is called when the root is visited
def index(request):
	response = "I am your first request!"
	return HttpResponse(response)

# Create your views here.
