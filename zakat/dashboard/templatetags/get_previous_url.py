from django import template
from avatar.models import Avatar


register = template.Library()


@register.simple_tag
def get_previous_url(request):
    return request.META.get('HTTP_REFERER')


@register.simple_tag
def get_avatar_id(user):
    try:
        return Avatar.objects.get(user__id=user.id).id
    except:
        return -1