""" platzigram views """
# Django
from django.http import HttpResponse, JsonResponse

from datetime import datetime

def hello(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('la hora bb {}'.format(now))

def sorted_numbers(request):
    """hi"""
   # import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbers.sort()
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'integers sorte'
    }
    return JsonResponse(data, json_dumps_params={'indent': 4})

def say_hi(request, name, age):
    """ say hai """
    if age < 12:
        message = "sorry {} papi pero no peudes entrar".format(name)
    else:
        message = "welcome {} yo le doy".format(name)
    return HttpResponse(message)

