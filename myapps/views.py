from random import randint
from django.http import HttpResponse
from articles.models import Articles


def home_view(request):
    """
    Take a simple request and respond with html elements
    :param request:
    :return:
    """
    obj = Articles.objects.get(id=2)
    name = 'Martin'
    numb = randint(0, 100000)
    HTML_ELEMENT = f'<h1>Hello mr. {name} for {numb} times on title: {obj.title}</h1>'
    return HttpResponse(HTML_ELEMENT)

