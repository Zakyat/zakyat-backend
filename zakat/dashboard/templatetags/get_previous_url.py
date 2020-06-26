from django import template

register = template.Library()

@register.simple_tag
def get_previous_url(request):
    return request.META.get('HTTP_REFERER')