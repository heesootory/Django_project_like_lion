from django import forms
from django.contrib.auth import get_user_model


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class UserCreateForm(UserBaseForm):
    password2 = forms.CharField(widget=forms.PasswordInput())
    # 비밀번호가 동일한지 확인

    class Meta(UserBaseForm.Meta):
        fields = ['username', 'email', 'phone', 'password']
