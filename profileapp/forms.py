

from django.forms import ModelForm
from profileapp.models import Profile
# account는 Form을 제공하지만 profile은 우리가 만든거라서 자체 제공 하지않음
# 그래서 ModelForm 기능을 이용하여 model을 Form으로 사용

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        # 사용할 fields 설정
        fields = ['image', 'nickname', 'message']
