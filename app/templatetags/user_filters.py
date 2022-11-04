from django import template

register=template.Library()

@register.filter()
def covert_to_lower(value):
    return value.lower()


@register.filter(name='rep')
def convert_to_replacechar(value,arg):
    return value.replace(arg,'G')


#register.filter('low',covert_to_lower)