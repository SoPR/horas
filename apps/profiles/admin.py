from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {
            'fields': ('featured', 'bio', 'city', 'state', 'twitter_username',
                       'facebook_username', 'github_username', 'website_url',
                       'gravatar_url', 'is_gravatar_verified', 'day_of_week',
                       'start_time', 'phone', 'skype', 'google',
                       'jitsi', 'address', 'tags', 'timezone')
        }),
    )


admin.site.register(User, CustomUserAdmin)
