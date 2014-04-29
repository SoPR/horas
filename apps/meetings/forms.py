# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms import Select
from django.utils.translation import ugettext_lazy as _

from .models import Meeting

class MeetingUpdateForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ('format', 'message')

    def __init__(self, *args, **kwargs):
        self.protege = kwargs.pop('protege')

        super(MeetingUpdateForm, self).__init__(*args, **kwargs)

        meeting = kwargs.get('instance')
        choices = [('', _('--- Selecciona ---'))]
        choices.extend(meeting.mentor.get_meeting_formats())
        self.fields['format'].widget = Select(choices=choices)
        self.fields['format'].required = True
        self.fields['format'].label = _('Formato')

        self.fields['message'].required = True
        self.fields['message'].label = _('Mensaje')
        self.fields['message'].help_text = _(u'En este mensaje, explica de que quieres hablar en la reunión, por qué escogiste a esta persona. Trata de dejarle saber al mentor los temas que quieres hablar durante la reunión. Piensa que el mentor se tiene que preparar y tu debes estar preparado antes de la reunión. Este mensaje debe ayudar a ambos a saber que esperar de la reunión.')

    def save(self, *args, **kwargs):
        meeting = super(MeetingUpdateForm, self).save(commit=False, *args, **kwargs)
        meeting.get_state_info().make_transition('reserve', self.protege)
        return meeting.save()
