from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

register = template.Library()


@register.filter("iconbool", is_safe=True)
def iconbool(value):
    """Given a boolean value, this filter outputs a font-awesome icon + the
    word "Yes" or "No"

    Example Usage:

        {{ user.has_widget|iconbool }}

    """
    file_path = settings.STATIC_URL

    if bool(value):
        result = '<img src="' + str(file_path) + 'img/icon-yes.svg"' + ' />'
    else:
        result = '<img src="' + str(file_path) + 'img/icon-no.svg"' + ' />'
    return mark_safe(result)
