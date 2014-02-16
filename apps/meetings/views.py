from django.views.generic import TemplateView


class MeetingDetailView(TemplateView):
    """
    Displays a specific meeting's details.
    """
    template_name = 'meetings/meeting_detail.html'
