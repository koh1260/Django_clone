from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # profile과 user객체를 하나씩 연결해줌.
    # on_delete: 연결 객체가 사라지면 연결된 profile 객체의 정책.
    # CASCADE: profile도 사라지게.
    # 더 많은 설정은 django document 참고.
    # related_name: request.user.profile 처럼 사용 가능하게 해주는 설정(외래키 연결하고 참조하는 거 같음).
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)