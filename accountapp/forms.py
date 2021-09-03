from django.contrib.auth.forms import UserCreationForm

# UserCreationForm 상속 받아서 수정하기

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # UserCrationForm 전체 상속
        super().__init__(*args, **kwargs)
        # change informattion에서 username부분 바꿀수 없게 수정
        self.fields['username'].disabled = True