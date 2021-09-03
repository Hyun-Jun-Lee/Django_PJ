from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"
urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),
    # class 형 view는 불러온후 .as_view() 붙여야함
    path('create/', AccountCreateView.as_view(), name='create'),
    # login view는 템플릿 지정해줘야함
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # detail 정보는 고유키(pk)필요
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

]