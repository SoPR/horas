# encoding: utf-8
from django import forms
from django.forms.utils import ErrorList
from django.utils import six
from django.utils.translation import ugettext_lazy as _
from taggit.utils import edit_string_for_tags

from .fields import DAYS_OF_WEEK
from .models import User

TIME_CHOICES = (
    ('00:00:00', '12:00 AM'),
    ('00:30:00', '12:30 AM'),
    ('01:00:00', '1:00 AM'),
    ('01:30:00', '1:30 AM'),
    ('02:00:00', '2:00 AM'),
    ('02:30:00', '2:30 AM'),
    ('03:00:00', '3:00 AM'),
    ('03:30:00', '3:30 AM'),
    ('04:00:00', '4:00 AM'),
    ('04:30:00', '4:30 AM'),
    ('05:00:00', '5:00 AM'),
    ('05:30:00', '5:30 AM'),
    ('06:00:00', '6:00 AM'),
    ('06:30:00', '6:30 AM'),
    ('07:00:00', '7:00 AM'),
    ('07:30:00', '7:30 AM'),
    ('08:00:00', '8:00 AM'),
    ('08:30:00', '8:30 AM'),
    ('09:00:00', '9:00 AM'),
    ('09:30:00', '9:30 AM'),
    ('10:00:00', '10:00 AM'),
    ('10:30:00', '10:30 AM'),
    ('11:00:00', '11:00 AM'),
    ('11:30:00', '11:30 AM'),
    ('12:00:00', '12:00 PM'),
    ('12:30:00', '12:30 PM'),
    ('13:00:00', '1:00 PM'),
    ('13:30:00', '1:30 PM'),
    ('14:00:00', '2:00 PM'),
    ('14:30:00', '2:30 PM'),
    ('15:00:00', '3:00 PM'),
    ('15:30:00', '3:30 PM'),
    ('16:00:00', '4:00 PM'),
    ('16:30:00', '4:30 PM'),
    ('17:00:00', '5:00 PM'),
    ('17:30:00', '5:30 PM'),
    ('18:00:00', '6:00 PM'),
    ('18:30:00', '6:30 PM'),
    ('19:00:00', '7:00 PM'),
    ('19:30:00', '7:30 PM'),
    ('20:00:00', '8:00 PM'),
    ('20:30:00', '8:30 PM'),
    ('21:00:00', '9:00 PM'),
    ('21:30:00', '9:30 PM'),
    ('22:00:00', '10:00 PM'),
    ('22:30:00', '10:30 PM'),
    ('23:00:00', '11:00 PM'),
    ('23:30:00', '11:30 PM'),
)


class TagWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, six.string_types):
            tags = [o.tag for o in value.select_related("tag")]
            value = edit_string_for_tags(tags)
        return super(TagWidget, self).render(name, value, attrs)


class SignupForm(forms.Form):
    full_name = forms.CharField(
        label=_("Nombre Completo"),
        max_length=60,
        widget=forms.TextInput(attrs={
            'placeholder': _('Nombre Completo'),
            'autofocus': 'autofocus'}))

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')

    def save(self, user):
        full_name = self.cleaned_data['full_name']
        user.first_name = full_name.split(' ')[0]
        user.last_name = " ".join(full_name.split(' ')[1:])

        user.save()


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'bio', 'tags', 'city', 'state',
                  'twitter_username', 'github_username', 'linkedin_url',
                  'website_url', 'skype', 'google', 'jitsi', 'phone',
                  'address', 'day_of_week', 'start_time', 'timezone')

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].label = _('Nombre')
        self.fields['first_name'].required = True

        self.fields['last_name'].label = _('Apellidos')
        self.fields['last_name'].required = True

        self.fields['bio'].label = _(u'Biografía corta')
        self.fields['bio'].required = True
        self.fields['bio'].widget = forms.Textarea(attrs={'rows': 3})
        self.fields['bio'].help_text = _('Maximo de 140 caracteres')

        self.fields['tags'].label = _('Lista de temas')
        self.fields['tags'].required = True
        self.fields['tags'].help_text = _('Separados por comas')
        self.fields['tags'].widget = TagWidget(attrs={
            'rows': 3,
            'placeholder': _(u'Ejemplo: diseño, programación, arte, ' +
                             u'música, activismo, educación')
        })

        self.fields['city'].label = _('Ciudad')
        self.fields['city'].required = True

        self.fields['state'].label = _('Estado')
        self.fields['state'].required = True

        self.fields['skype'].widget = forms.TextInput(
            attrs={'placeholder': _('usuario')})

        self.fields['google'].label = _('Google Hangout')

        self.fields['phone'].label = _(u'Teléfono')

        self.fields['address'].label = _(
            u'Dirección para reuniones en persona')
        self.fields['address'].widget = forms.Textarea(
            attrs={
                'rows': 3,
                'placeholder': _(u'Entra una dirección física ' +
                                 '- http://maps.google.com/123')
                })

        self.fields['day_of_week'].widget = forms.RadioSelect(
            choices=DAYS_OF_WEEK)
        self.fields['day_of_week'].required = True

        self.fields['start_time'].label = _(u'Hora del día')
        self.fields['start_time'].required = True
        self.fields['start_time'].widget = forms.Select(choices=TIME_CHOICES)
        if not self.initial['start_time']:
            self.initial['start_time'] = TIME_CHOICES[24][0]

        self.fields['timezone'].label = _(u'Zona horaria')
        self.fields['timezone'].required = True

    def clean_bio(self, *args, **kwargs):
        bio = self.cleaned_data['bio']
        if len(bio) > 140:
            raise forms.ValidationError('')
        return bio

    def clean_tags(self, *args, **kwargs):
        tags = self.cleaned_data['tags']
        return [t.lower() for t in tags]

    def clean_day_of_week(self, *args, **kwargs):
        if self.cleaned_data['day_of_week'] == '':
            raise forms.ValidationError(_('Debes escoger un día'))
        return self.cleaned_data['day_of_week']

    def clean(self):
        cleaned_data = super(ProfileUpdateForm, self).clean()
        formats = [
            False if cleaned_data.get('phone') == '' else True,
            False if cleaned_data.get('skype') == '' else True,
            False if cleaned_data.get('google') == '' else True,
            False if cleaned_data.get('jitsi') == '' else True,
            False if cleaned_data.get('address') == '' else True
        ]

        if any(formats) == False:
            self.errors['phone'] = ErrorList([u''])
            self.errors['skype'] = ErrorList([u''])
            self.errors['google'] = ErrorList([u''])
            self.errors['jitsi'] = ErrorList([u''])
            self.errors['address'] = ErrorList([u''])

            raise forms.ValidationError(
                _(u'Es necesario registrar por lo menos un formato ' +
                u'de reunión. Teléfono, Skype, Google, Jitsi o ' +
                u'En persona.'))

        return cleaned_data
