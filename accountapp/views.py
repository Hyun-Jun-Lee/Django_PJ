from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

#함수형 뷰
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
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # reverse : 함수, reverse_lazy : 클래스
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    # reverse : 함수, reverse_lazy : 클래스
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'