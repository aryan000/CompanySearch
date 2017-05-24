from django.shortcuts import render
from django.http import HttpResponse
import json
import os

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def test(request) :
	Context = {'polarity':'positive','name':'Nidhi','type':'string'}
	return render(request, 'review.html', Context)

# def home(request) :
# 	return render(request, 'home.html')


def main(request):
    if 'company_name' in request.GET : 
        company_name = request.GET['company_name']
        print( " hello getting is : " +  company_name )
        print (os.path.join(os.getcwd()))
        with open('company_dict1.json' , 'r') as f:
            data = json.load(f)
        return render(request , 'main1.html',data)
    return render(request,'navbar.html')

     

def company_search(request) :
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            message = 'You searched for: %r' % request.GET['q']
            return HttpResponse(message)
    return render(request, 'home.html', {'error': error})
	# if 'q' in request.GET:
	# 	message = 'You searched for: %r' % request.GET['q']
	# else:
	#     message = 'You submitted an empty form.'
	# return HttpResponse(message)
#return render(request, 'comapany_search.html')


def feature(request,company_name):

    print ("\n\n\n\ncompany name is : " + company_name)
    # company_name = request.GET['company_name']
    with open('company_dict1.json' , 'r') as f:
        data = json.load(f)
    return render(request , 'feature.html',data)

    
