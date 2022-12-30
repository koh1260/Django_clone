from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ProfileCreationForm
from .models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # profileform에서 받은 데이터가 form에 들어 있음.
        # commit=False: 임시 저장.
        temp_profile = form.save(commit=False)
        # user 데이터는 아직 없음.
        # profile의 user를 현재 페이지를 보고 있는 당사자의 user로 한다.
        temp_profile.user = self.request.user
        # 최종 저장.
        temp_profile.save()

        # 기존 함수
        return super().form_valid(form)
