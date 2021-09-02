from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


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
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})

