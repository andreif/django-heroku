from django.http import HttpResponse
import dmsl
  
def home(request):
    content = 'Hello World'
    res = dmsl.Template('index.dmsl').render(locals())
    return HttpResponse(res)
