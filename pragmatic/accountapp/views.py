from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from .forms import AccountUpdateForm
from .models import HelloWorld
from django.urls import reverse, reverse_lazy


# Create your views here.


def hello_world(request):
    # 로그인이 되어 있다면 hello world 페이지 보여주고 그렇지 않다면 login 페이지로 redirect
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    # 사용할 테이블
    model = User
    # 폼
    form_class = UserCreationForm
    # 사용자 이름
    context_object_name = 'target_user'
    # 성공시 이동할 페이지
    success_url = reverse_lazy('accountapp:hello_world')
    # 사용할 템플릿
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs):
        # self는 AccountupdateView를 가리킴.
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            # return HttpResponseRedirect(reverse('accountapp:login'))
            # 금지된 곳에 접근한 것을 알림 403 error.
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))
