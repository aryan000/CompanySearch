from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
	# url(r'^test/', views.test, name = 'test'),
	# url(r'^home/$', views.home, name = 'home'),
	url(r'^company_search/$', views.company_search, name = 'comapny_search') ,
	url(r'^main/$' , views.main , name = "main")  ,
	url(r'^feature/(?P<company_name>[-\w]+)/$', views.feature , name = "feature") 
	
]