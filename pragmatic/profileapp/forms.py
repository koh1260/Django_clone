from django.forms import ModelForm

from .models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        # user는 서버에서 처리.
        fields = ['image', 'nickname', 'message']