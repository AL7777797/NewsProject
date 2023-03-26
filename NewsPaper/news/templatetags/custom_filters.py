"""
Я не придумал, как это сделать...

from django import template

register = template.Library()


@register.filter()
def censored(value):
    for word in value:
        if word == "редиска" or "Редиска":
            fixed_word = "***"
            return f'{fixed_word}'