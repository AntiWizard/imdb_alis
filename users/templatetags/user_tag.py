from django import template

register = template.Library()


@register.filter(name="custom", is_safe=True)
def custom(value):
    value = str(value)
    if "@" in value:
        return value.split("@")[0]
    else:
        return value
