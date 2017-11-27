from django.http import HttpResponse
from random import randint

@require_http_methods("GET ")
def rangGen():
    num = randint(0, 99999)
    html = "<html><body></body>%s</html>" % num
    return HttpResponse(html)