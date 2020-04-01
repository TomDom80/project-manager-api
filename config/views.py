from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from subprocess import call


@csrf_exempt
def giupulloriginmaster(request):
    ret = 'updating...'
    print(ret)
    call_text = 'git pull origin master'
    call(call_text, shell=True)
    call_text = 'devil www restart mapi.ct8.pl'
    call(call_text, shell=True)

    return HttpResponse(ret)
