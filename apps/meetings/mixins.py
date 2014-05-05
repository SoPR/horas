from django.http import HttpResponseForbidden


class RestrictToMentorMixin(object):
    def get_object(self, *args, **kwargs):
        self.object = super(RestrictToMentorMixin, self).get_object(*args, **kwargs)

        if self.request.user != self.object.mentor:
            return HttpResponseForbidden()

class RestrictToProtegeMixin(object):
    def get_object(self, *args, **kwargs):
        self.object = super(RestrictToProtegeMixin, self).get_object(*args, **kwargs)

        if self.request.user != self.object.protege:
            return HttpResponseForbidden()

class RestrictToParticipantsMixin(object):
    def get_object(self, *args, **kwargs):
        self.object = super(RestrictToParticipantsMixin, self).get_object(*args, **kwargs)

        if (self.request.user != self.object.mentor or
            self.request.user != self.object.protege):

            return HttpResponseForbidden()
