from django  import template

register = template.Library()

@register.filter (name = "get_from_dict")
def keyvalue(dict, key):    
    return dict[key] 

@register.filter(name = "get_inner_dict")

def keyvalue(dict,key1,key2):
	return dict[key1][key2]