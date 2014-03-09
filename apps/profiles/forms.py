from django import forms
from django.utils.translation import ugettext_lazy as _


class SignupForm(forms.Form):
    full_name = forms.CharField(
        label=_("Full name"),
        max_length=60,
        widget=forms.TextInput(attrs={
            'placeholder': _('Full name'),
            'autofocus': 'autofocus'}))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')

    def save(self, user):
        full_name = self.cleaned_data['full_name']

        user.first_name = full_name.split(' ')[0]
        user.last_name = " ".join(full_name.split(' ')[1:])

        user.save()
