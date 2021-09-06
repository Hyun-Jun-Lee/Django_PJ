from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article
from projectapp.models import Project


def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # request로 요청한 user의 pk
        project = Project.objects.get(pk=kwargs['pk'])
        if not project.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated