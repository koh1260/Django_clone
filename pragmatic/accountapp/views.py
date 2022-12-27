from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import HelloWorld
from django.urls import reverse

# Create your views here.


def hello_world(request):

    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        # 객체(데이터) 생성
        new_hello_world = HelloWorld()
        # 데이터의 text 컬럼에 temp 대입.
        new_hello_world.text = temp
        # 저장
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'text': 'No DATA!!!', 'hello_world_list' : hello_world_list})

