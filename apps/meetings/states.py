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

    class confirmed(StateDefinition):
        description = _('Confirmed')

    class cancelled(StateDefinition):
        description = _('Cancelled')

    class didnt_happened(StateDefinition):
        description = _('Meeting didn\'t happened')

    class completed(StateDefinition):
        description = _('Completed')


    # state transitions
    class reserve(StateTransition):
        from_state = 'available'
        to_state = 'reserved'
        description = _('When a protege asks for the meeting')

        def handler(transition, instance, user):
            instance.protege = user
            instance.save()

            notification.send(
                [instance.mentor],
                'reserved_meeting_slot',
                {'meeting': instance})

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
            instance.cancelled_by = user
            instance.save()

    class cancel_confirmed(StateTransition):
        from_state = 'confirmed'
        to_state = 'cancelled'
        description = _('When mentor or protege cancels a confirmed meeting')

        def handler(transition, instance, user):
            instance.cancelled_by = user
            instance.save()

    class didnt_happened_reserved(StateTransition):
        from_state = 'reserved'
        to_state = 'didnt_happened'
        description = _('When the meetings is not held after being reserved')

    class didnt_happened_confirmed(StateTransition):
        from_state = 'confirmed'
        to_state = 'didnt_happened'
        description = _('When the meetings is not held after being confirmed')

    class complete(StateTransition):
        from_state = 'confirmed'
        to_state = 'completed'
        description = _('When mentor or protege confirms the meeting was held')
