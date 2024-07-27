from django import template
import datetime

register=template.Library()
@register.simple_tag(name="today")
def get_today():
    n=datetime.datetime.now()
    return n
