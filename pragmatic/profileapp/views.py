from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from .decorators import profile_ownership_required
from .forms import ProfileCreationForm
from .models import Profile
from django.urls import reverse


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/create.html'

    #detail 페이지로 가려면 pk 값이 있어야하는데, 클래스에 연관된 파라미터를 넘겨주기 떄문에 줄 수가 없음.
    # 따라서 get_succecss_url 을 오버라이딩.
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})
    # self.object는 Profile이다.
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

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})

