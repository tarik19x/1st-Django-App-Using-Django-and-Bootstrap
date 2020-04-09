from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')

def removepunc(request):

    # print(request.GET.get('opinion','default'))
    text=request.GET.get('opinion','default')
    t="~!@#$%^&*()_+<>?/{}|]["
    k=""
    cnt=0
    cntr=0
    if request.GET.get("add_or_not" )=='on':
        cnt=1
        for i in text:
            if i not in t:
                 k+=i

        text=k
        k=""
    
    if request.GET.get("capitalized" )=='on':
        cnt=1
        for i in text:
            k+=i.capitalize()
        text=k
        k=""

    if request.GET.get("bits_only" )=='on':
        cnt=1
        res = ''.join(format(ord(i), 'b') for i in text) 
        k= str(res)
        text=k
        k=""

    if request.GET.get("counter" )=='on':
        cnt=1
        for i in text:
              cntr+=1
        text=cntr

    if cnt==0:
        k=text
    print("***************************************************",k)
    kajer_jinish={'Text':text}
    return render(request,'text.html',kajer_jinish)








def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")