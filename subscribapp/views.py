from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk' : self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):

        # get_object_or_404 : pk를 찾지 못햇다면 404 응답
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    template_name = 'subscribeapp/list.html'
    context_object_name = 'article_list'
    paginate_by = 8

    def get_queryset(self):
        # Subscription 모델에서 user의 project값을 list로 받기
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        # __(duble underscore) : filed lookup
        article_list = Article.objects.filter(project__in=projects)
        return article_list