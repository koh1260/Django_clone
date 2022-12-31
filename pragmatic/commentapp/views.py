from django.shortcuts import render
from django.views.generic import CreateView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


# Create your views here.
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        # save(commit=False): commit=False의 원래 기능은 db save를 지연시켜 중복 저장을 막는 거지만,
        # 보통 db에 저장하기 전 일련의 작업을 하고 싶을 쌔 사용.
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        from django.urls import reverse
        return reverse('articleapp:detail', kwargs={'pk' : self.object.article.pk})