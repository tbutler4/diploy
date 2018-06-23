from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def test(request):
	response = "Hello, I am test"
	return HttpResponse(response)

def john(request):
	response = "placeholder to later display all the list of blogs"
	return HttpResponse(response)\

def new(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def show(request, number):
	print (number)
	return HttpResponse("placeholder to display blog" + number)
