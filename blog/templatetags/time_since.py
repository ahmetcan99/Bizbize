from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def time_since(value):
    now = timezone.now()
    diff = now - value

    if diff.days > 0:
        return f'{diff.days} gün önce'
    elif diff.seconds > 3600:
        return f'{diff.seconds // 3600} saat önce'
    else:
        return f'{diff.seconds // 60} dakika önce'