from django import forms

from users.models import User


class BaseAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('date_of_birth', 'passport_number', 'phone_number')
        help_texts = {
            'phone_number': 'Номер в формате +7XXXXXXXXXX',
            'passport_number': 'Номер в формате ХХХХ ХХХХХХ',
            'date_of_birth': 'ГГГГ-ММ-ДД'
        }


class AdminUserCreationForm(BaseAdminForm):
    """Форма для создания пароля и других данных"""

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AdminCustomUserChangeForm(BaseAdminForm):
    """Форма для изменения пароля и других данных"""
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        required=False
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["password"]:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
