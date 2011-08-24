from django.shortcuts import render_to_response

def home(request):
    content = 'Hello World'
    return render_to_response('index.html', locals())
