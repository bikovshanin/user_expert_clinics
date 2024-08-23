from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from users.forms import AdminCustomUserChangeForm, AdminUserCreationForm
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Кастомная админская конфигурация для модели пользователя (User).

    Определяет, как модель пользователя будет отображаться и управляться в
    админ-панели Django.

    """
    add_form = AdminUserCreationForm
    form = AdminCustomUserChangeForm

    list_display = ('id', 'email',)

    readonly_fields = ('date_joined', 'last_login',)

    search_fields = ('first_name', 'last_name', 'email', 'phone_number',)
    search_help_text = 'Поиск по имени, фамилии, почте, номеру телефона'

    fieldsets = (
        (None, {
            'classes': ['extrapretty'],
            'fields': (
                'email',
                'first_name',
                'last_name',
                'middle_name',
                'phone_number',
                'date_of_birth',
                'passport_number',
                'place_of_birth',
                'registration_address',
                'residence_address',
                'password',  # Поле для пароля
                'is_staff',
                'is_superuser',
                'date_joined',
                'last_login',
            )
        }),
        ('Permissions', {
            'classes': ['collapse'],
            'fields': (
                'groups',
                'user_permissions',
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ['extrapretty'],
            'fields': (
                'email',
                'first_name',
                'last_name',
                'middle_name',
                'phone_number',
                'date_of_birth',
                'passport_number',
                'place_of_birth',
                'registration_address',
                'residence_address',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
            )
        }),
    )

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs['form'] = self.add_form
        else:
            kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return self.fieldsets
