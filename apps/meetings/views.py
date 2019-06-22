from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, FormView, UpdateView

from apps.comments.models import Comment

from .forms import MeetingCommentCreationForm, MeetingUpdateForm
from .models import Meeting


class MeetingDetailView(DetailView):
    model = Meeting

    def get_object(self, *args, **kwargs):
        return get_object_or_404(
            Meeting.objects.select_related('mentor', 'protege'),
            pk=self.kwargs.get('pk'),
            mentor__username=self.kwargs['username'])

    def get_context_data(self, *args, **kwargs):
        ctx = super(MeetingDetailView, self).get_context_data(*args, **kwargs)
        user = self.object.mentor
        ctx['meeting_format_information'] = self.object.mentor.get_meeting_format_information(self.object.format)
        ctx['meeting_format_name'] = self.object.mentor.get_meeting_format_name(self.object.format)
        ctx['profile_user'] = user

        comment_type = ContentType.objects.get(app_label='meetings', model='meeting')
        ctx['comments'] = Comment.objects.select_related('user').filter(
            content_type=comment_type, object_id=self.object.id)

        return ctx


class MeetingUpdateView(LoginRequiredMixin, UpdateView):
    model = Meeting
    form_class = MeetingUpdateForm

    def get_object(self, *args, **kwargs):
        return get_object_or_404(
            Meeting.objects.select_related('mentor', 'protege'),
            pk=self.kwargs.get('pk'), state='available',
            mentor__username=self.kwargs['username'])

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(MeetingUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['protege'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        ctx = super(MeetingUpdateView, self).get_context_data(*args, **kwargs)
        user = self.object.mentor
        ctx['profile_user'] = user
        return ctx

    def get_success_url(self):
        return reverse_lazy('profile_detail',
                            args=[self.kwargs['username']])


class MeetingConfirmView(LoginRequiredMixin, UpdateView):
    model = Meeting
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        self.object.get_state_info().make_transition('confirm', self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, *args, **kwargs):
        '''
        Only the mentor of the meeting can confirm
        '''
        return get_object_or_404(
            Meeting.objects.select_related('mentor', 'protege'),
            pk=self.kwargs.get('pk'), mentor=self.request.user, state='reserved')

    def get_success_url(self):
        return reverse_lazy('profile_detail',
                            args=[self.kwargs['username']])


class MeetingCancelView(LoginRequiredMixin, UpdateView):
    model = Meeting
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        trans_name = 'cancel_{}'.format(self.object.state)
        self.object.get_state_info().make_transition(trans_name, self.request.user)

        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, *args, **kwargs):
        '''
        Both mentor and protege can cancel a meeting
        '''
        return get_object_or_404(
            Meeting.objects.select_related('mentor', 'protege'),
            Q(mentor=self.request.user) | Q(protege=self.request.user),
            Q(state='reserved') | Q(state='confirmed'), pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse_lazy('profile_detail',
                            args=[self.kwargs['username']])


class MeetingCommentView(FormView):
    form_class = MeetingCommentCreationForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Comentario publicado'))
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, _('Fomulario de comentario incomleto'))
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(MeetingCommentView, self).get_form_kwargs(*args, **kwargs)

        self.meeting = Meeting.objects.get(
            mentor__username=self.kwargs['username'], pk=self.kwargs['pk'])

        kwargs.update({
            'meeting': self.meeting,
            'user': self.request.user
        })

        return kwargs

    def get_success_url(self):
        return reverse_lazy('meeting_detail',
                            args=[self.kwargs['username'], self.kwargs['pk']])
