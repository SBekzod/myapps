import random
from django.http import HttpResponse


def home_view(request):
    """
    Take a simple request and respond with html elements
    :param request:
    :return:
    """
    name = 'Martin'
    numb = random.randint(0, 100000)
    HTML_ELEMENT = f'<h1>Hello mr. {name} for {numb} times</h1>'
    return HttpResponse(HTML_ELEMENT)

