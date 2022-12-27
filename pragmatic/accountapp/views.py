from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView

from .models import HelloWorld
from django.urls import reverse, reverse_lazy


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
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'