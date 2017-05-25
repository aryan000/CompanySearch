from django  import template
from DateTime import DateTime
import string 
import re
register = template.Library()

@register.filter (name = "get_from_dict")
def keyvalue(dict, key):    
    return dict[key] 

@register.filter(name ="sentiment_filter")
def get_sentiment(sentiment):
	sentiment = str(sentiment)
	options = { '-2' : 'Very Negative ' , '-1' : 'Negative ' , '0' : 'Neutral' , '1' : 'Positive ' , '2' : 'Very Positive' }
	# print("present sentiment is : " + sentiment + " and returning " + options[sentiment])
	return options[sentiment]	


@register.filter(name="date_filter")
def get_date(date):
	date = str(date) 

	if(len(date)==0):
		return "Not Specified"
	x = DateTime(date)
	new_date = ""
	new_date += x.Day() + '  ' + str(x.day()) + '  ' + x.Month()  + '  ' + str(x.year())
	print("new date is : " + str(new_date))
	return new_date


@register.filter(name = "caps_filter")
def get_caps(word):
	return string.capwords(word) 


@register.filter(name = "remove_quotes")
def remove_quote(word):
	s = re.sub(r'^"*|"*$', '', word)
	return s


@register.filter(name = "remove_and")
def remove_and(word):
	s = re.sub(r'&amp;','&', word)
	return s

