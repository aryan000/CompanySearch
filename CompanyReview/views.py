from django.shortcuts import render
from django.http import HttpResponse
from DateTime import DateTime
import json
import os
import random
import django
import datetime

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter,datestr2num

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




def chart(request,company_name):
    print ("company name is : " + company_name)
    # company_name = request.GET['company_name']
    with open('data.json' , 'r') as f:
        data = json.load(f)
        data['name' ] = company_name

    print (data)
    return render(request,'charts.html', data)




def simple_chart(request,company_name):
    with open('data.json' , 'r') as f:
        data = json.load(f)
        data['name' ] = company_name

    fig=Figure(figsize=(11,6))
    ax=fig.add_subplot(1,1,1)
    x=[]
    y=[] 

    for i in data['yearlydata'] : 
        print(i + " and " + str(data['yearlydata'][i]['sentiment']))
        # print("\n|n")
        # x.append( datestr2num(i.split('to')[0]))
        y.append(data['yearlydata'][i]['sentiment'])
        y.append(data['yearlydata'][i]['sentiment'])
        a,b = i.split('to')
        x.append(datestr2num(a))
        x.append(datestr2num(b))
        # print("printing" + DateTime(data['yearlydata'][i]['sentiment'].split('to')[0]))
        # y.append(i['sentiment'])
    
    # x = [6,2,3,4,5,6,7,8]
    print(x)
    print(y)

    
    # now=datetime.datetime.now()
    # delta=datetime.timedelta(days=1)
    # for i in range(10):
        # x.append(now)
        # now+=delta
        # y.append(random.randint(0, 1000))
    
    # for  i in range(0,5):
        # print( str(x[i]) + " and " + str(y[i]))

    ax.plot_date(x, y, '-')
    ax.set_xlabel('Half Yearly Data')
    ax.set_ylabel('Reviews')
    ax.set_title('Graphical View')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

    
