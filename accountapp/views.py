from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

# 데코레이터를 배열로 만들어서 코드 줄이기 가능
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

# 로그인 했는지 확인해주는 데코레이터
@login_required
def hello_world(request):

    if request.method == "POST":
        # POST에서 'hello_world_input' 라는 데이터를 가져오기
        temp = request.POST.get('hello_world_input')

        # models.py에서 model 가져오기
        new_hello_world = HelloWorld()
        # input 받은 데이터를 HelloWorld 모델의 text 라는 속성에 저장
        new_hello_world.text = temp
        # 저장
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})



# class형 view

# method_decorator : 데코레이터를 메서드에 사용할수잇도록 변환해주는 데코레이터
# method_decorator 활용해서 login_required를 get,post에 적용

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # reverse : 함수, reverse_lazy : 클래스
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    # reverse : 함수, reverse_lazy : 클래스
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'