from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
	url(r'^main/$' , views.main , name = "main")  ,
	url(r'^feature/(?P<company_name>[-\w]+)/$', views.feature , name = "feature") ,
	url(r'^chart/(?P<company_name>[-\w]+)/$' , views.chart , name = "chart"),
	url(r'^simple_chart/(?P<company_name>[-\w]+)/$' , views.simple_chart , name = "simple_chart"),
	url(r'^main/(?P<company_name>[-\w]+)/$' , views.main1, name = "main1"),
	url(r'^reviews/(?P<company_name>[-\w]+)/$' , views.reviews, name = "reviews")

	
]