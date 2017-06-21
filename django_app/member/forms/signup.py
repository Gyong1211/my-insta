from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '아이디'
            }
        )
    )
    nickname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '닉네임'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호 확인'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                '이미 존재하는 아이디입니다.'
            )
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if nickname and User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError(
                '이미 존재하는 닉네임입니다.'
            )
        return nickname

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError(
                '비밀번호를 다르게 입력했습니다.'
            )
        return password2

    def create_user(self):
        username = self.cleaned_data['username']
        nickname = self.cleaned_data['nickname']
        password = self.cleaned_data['password2']
        user = User.objects.create_user(
            username=username,
            nickname=nickname,
            password=password,
        )
        return user
