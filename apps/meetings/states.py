'''
Possible states
---------------

available:
    A new meeting.

reserved:
    A meeting that was available and reserved by protege.

confirmed:
    A meeting that was reserved by a protege and later accepted
    by the meeting's mentor.

cancelled:
    A meeting that was either reserved or confirmed and
    then cancelled by the mentor or protege.

unused:
    at least 1 hour have passed from the meeting's start datetime
    and the meeting is still in the available state, meaning
    it was not reserved by a protege.

deleted:
    A meeting in available state can be transitioned to deleted
    by the system after a user updates his/her meeting settings.
    This transition will produce a new available meeting.

'''

from django.utils.translation import ugettext_lazy as _

from django_states.machine import StateMachine, StateDefinition, StateTransition
from notification import models as notification


class MeetingStateMachine(StateMachine):
    log_transitions =  True

    # possible states
    class available(StateDefinition):
        description = _('Available')
        initial = True

    class reserved(StateDefinition):
        description = _('Reserved')

        def handler(self, instance):
            notification.send(
                [instance.mentor],
                'reserved_meeting_slot',
                {'meeting': instance})

    class confirmed(StateDefinition):
        description = _('Confirmed')

        def handler(self, instance):
            notification.send(
                [instance.protege],
                'confirmed_meeting',
                {'meeting': instance})

    class cancelled(StateDefinition):
        description = _('Cancelled')

        def handler(self, instance):
            if instance.cancelled_by_mentor():
                # Send message to protege
                notification.send(
                    [instance.protege],
                    'cancelled_by_mentor',
                    {'meeting': instance})

            if instance.cancelled_by_protege():
                # Send message to mentor
                notification.send(
                    [instance.mentor],
                    'cancelled_by_protege',
                    {'meeting': instance})

            instance.mentor.get_or_create_meeting()

    class unused(StateDefinition):
        description = _('Un-used')

    class deleted(StateDefinition):
        description = _('Deleted')


    # state transitions
    class reserve(StateTransition):
        from_state = 'available'
        to_state = 'reserved'
        description = _('When a protege asks for the meeting')

        def handler(transition, instance, user):
            instance.protege = user
            instance.save()

        def has_permission(transition, instance, user):
            return instance.mentor != user

    class confirm(StateTransition):
        from_state = 'reserved'
        to_state = 'confirmed'
        description = _('When the mentor accepts the meeting')

        def has_permission(transition, instance, user):
            if instance.mentor == user:
                return True
            return False

    class cancel_reserved(StateTransition):
        from_state = 'reserved'
        to_state = 'cancelled'
        description = _('When mentor or protege cancels a reserved meeting')

        def handler(transition, instance, user):
            instance.save()

        def has_permission(transition, instance, user):
            if user in [instance.mentor, instance.protege]:
                return True
            return False

    class cancel_confirmed(StateTransition):
        from_state = 'confirmed'
        to_state = 'cancelled'
        description = _('When mentor or protege cancels a confirmed meeting')

        def handler(transition, instance, user):
            instance.save()

        def has_permission(transition, instance, user):
            if user in [instance.mentor, instance.protege]:
                return True
            return False

    class flag_unused(StateTransition):
        from_state = 'available'
        to_state = 'unused'
        description = _('When a meeting was never reserved by a protege')

    class delete(StateTransition):
        from_state = 'available'
        to_state = 'deleted'
        description = _('When the user change settings we destroy available meetings')
