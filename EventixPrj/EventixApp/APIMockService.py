from EventixApp.models import *


class APIMockService:
    def GetEvent(eventGuid):
        return Event.objects.get(guid=eventGuid)

    def GetEventTickets(eventGuid):
        return Ticket.objects.get(event_id=eventGuid)
