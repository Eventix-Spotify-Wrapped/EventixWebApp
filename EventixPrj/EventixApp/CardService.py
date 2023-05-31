from EventixApp.models import *


class CardService:
    def GetWrapCards(wrapGuid):
        return Card.objects.get(id=wrapGuid)

    def GetCardWrap(cardGuid):
        return Wrap.objects.get(
            id=getattr(Card.objects.get(id=cardGuid), Card._meta.get_field(id).attname)
        )


# from enum import Enum


# class DayOfWeek(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7


# class Cards:
#     def PerDayOfWeek(username, startDate, endDate, dayOfWeek):
#         if live:
#             events = apimanager.GetEventsFromTimeframe(username, startdate, enddate)
#         else:
#             events = models.events
#         for event in events:
#             if event.day == "Friday":
#                 ticketsales

#         dayOfWeek = Enum("DayOfWeek", [""])


# cards = [ticketssoldfridays, ticketssoldweekends, ticketssoldmidnight]
