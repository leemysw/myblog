from django import template

from ..models import User

register = template.Library()


@register.simple_tag()
def is_confirm(user):
    user = User.objects.get(user=user)
    isconfirm = user.confirmed
    return isconfirm
