from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import pandas as pd
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# User#


class Organizer(models.Model):
    guid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)


# Coupon#
class Coupon(models.Model):
    guid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    CHEQUE = "CH"
    FIXED_DISCOUNT = "FD"
    PERCENTAGE_DISCOUNT = "PD"
    NEW_PRICE = "NP"
    type = [
        (CHEQUE, "cheque"),
        (FIXED_DISCOUNT, "fixed-discount"),
        (PERCENTAGE_DISCOUNT, "percentage-discount"),
        (NEW_PRICE, "new_price"),
    ]


class CouponCode(models.Model):
    code = models.CharField(max_length=4)
    coupon_guid = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    used_count = models.IntegerField()


# USEFUL?#
class CouponCodeCreate(models.Model):
    code = models.CharField(max_length=4)


# Event #
class Event(models.Model):
    guid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ONCE = "ON"
    REPEATING = "RP"
    type = [(ONCE, "once"), (REPEATING, "repeating")]
    UNAVAILABLE = "UNA"
    AVAILABLE = "AVA"
    SOLD_OUT = "SO"
    REFUNDING = "RF"
    MOVING = "MV"
    status = [
        (UNAVAILABLE, "unavailable"),
        (AVAILABLE, "available"),
        (SOLD_OUT, "sold-out"),
        (REFUNDING, "refunding"),
        (MOVING, "moving"),
    ]


class EventDate(models.Model):
    guid = models.AutoField(primary_key=True)
    start = models.CharField(max_length=100)


class EventLocation(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9999999999)]
    )
    address = models.CharField(max_length=65536)
    public = models.BooleanField


# Shop#


class Shop(models.Model):
    guid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


# Location#


class Location(models.Model):
    latitude = models.FloatField
    longitude = models.FloatField
    count = models.IntegerField


# Ticket#
class Ticket(models.Model):
    guid = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    increment = models.IntegerField


# Authenticator#


class OAuthClient(models.Model):
    id = models.AutoField(primary_key=True)
    secret = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    updated_at = models.CharField(max_length=100)


# Cards #


class Post(models.Model):
    text = models.CharField(max_length=280)
    date_posted = models.DateTimeField(auto_now_add=True)


class Wrap(models.Model):
    id = models.AutoField(primary_key=True)
    # account manager
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # event organizer
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    wrap = models.ForeignKey(Wrap, on_delete=models.CASCADE)
    context = models.JSONField(default=list)


# Transaction #
# class Transaction(models.Model):
#     order_id = models.CharField(primary_key=True)
#     shop_name = models.CharField(max_length=255)
#     event_name = models.CharField(max_length=255)
#     event_category = models.CharField
#     event_subcategory = models.CharField
#     first_event = models.CharField
#     last_event = models.CharField
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     ticket_name = models.CharField(max_length=255)
#     barcode = models.CharField
#     order_status = models.CharField(max_length=15)
#     order_invalidated = None
#     order_invalidated_at = None
#     ticket_invalidated = None
#     ticket_invalidated_at = None
#     created_at = models.CharField
#     paid_currency = models.FloatField
#     order_value = models.FloatField
#     order_fees = models.FloatField
#     transaction_fees = models.FloatField
#     ticket_value = models.FloatField
#     ticket_fees = models.FloatField
#     optionals_value = models.FloatField
#     refunded_amount = models.FloatField
#     payment_id = None
#     payment_method = None
#     coupons = None
#     device = models.CharField(max_length=15)
#     tracker = None
#     tracker_name = None
#     seat = None
#     is_scanned = models.BooleanField
#     first_scanned_at = models.CharField
#     order_metadata_first_name = None
#     order_metadata_last_name = None
#     order_metadata_wrong1 = None
#     order_metadata_wrong2 = None
#     order_metadata_wrong3 = None
#     order_metadata_wrong4 = None
#     order_metadata_wrong5 = None
#     order_metadata_wrong6 = None
#     order_metadata_wrong7 = None
#     order_metadata_wrong8 = None
#     order_metadata_city = models.CharField(max_length=15)
#     order_metadata_gender = models.CharField
#     order_metadata_province = models.CharField
#     order_metadata_company = None
#     order_metadata_country = models.CharField
#     order_metadata_covid_no_symptoms = None
#     order_metadata_age = models.IntegerField(
#         validators=[MinValueValidator(10), MaxValueValidator(120)]
#     )
#     order_metadata_wrong9 = None
#     order_metadata_wrong10 = None
#     order_metadata_wrong11 = None
#     order_metadata_wrong12 = None
#     order_metadata_wrong13 = None
#     order_metadata_wrong14 = None
#     order_ticket_metadata_first_name = None
#     order_ticket_metadata_last_name = None
#     order_ticket_wrong1 = None
#     order_ticket_metadata_email = None
#     order_ticket_metadata_street = None
#     order_ticket_metadata_street_number = None
#     order_ticket_metadata_street_number_additional = None
#     order_ticket_metadata_postal = None
#     order_ticket_metadata_date_of_birth = None
#     order_ticket_metadata_state = None
#     order_ticket_metadata_city = None
#     order_ticket_metadata_gender = None
#     order_ticket_metadata_province = None
#     order_ticket_metadata_company = None
#     order_ticket_metadata_country = None
#     order_ticket_metadata_covid_no_symptoms = None
#     order_ticket_metadata_age = None
#     order_ticket_wrong2 = None
#     order_ticket_metadata_phone = None
#     order_ticket_metadata_fullname = None
#     order_ticket_metadata_covid_one_household = None
#     order_ticket_metadata_keep_me_informed = None
#     order_ticket_metadata_Diet = None
#     geolocation_street_name = None
#     geolocation_street_number = None
#     geolocation_locality = None
#     geolocation_postal_code = None
#     geolocation_sub_locality = None
#     geolocation_admin_level_1 = None
#     geolocation_admin_level_2 = None
#     geolocation_country_code = None
#     geolocation_latitude = None
#     geolocation_longitude = None
#     ticket_pdf_link = None
#
#
#
#     def __init__(self, *args, **kwargs):
#             # accept any additional attributes as keyword arguments
#             super().__init__(*args, **kwargs)

class Transaction:
    def __init__(self, order_id, shop_name, event_name, event_category, first_event, last_event, first_name, last_name,
                 email, ticket_name, barcode, order_status, order_invalidated, order_invalidated_at, ticket_invalidated,
                 ticket_invalidated_at, created_at, paid_currency, order_value, order_fees, transaction_fees, ticket_value,
                 ticket_fees, optionals_value, refunded_amount, payment_method, coupons, device, tracker, tracker_name,
                 seat, is_scanned, first_scanned_at, order_metadata_first_name, order_metadata_last_name,
                 order_metadata_wrong1, order_metadata_wrong2, order_metadata_wrong3, order_metadata_wrong4,
                 order_metadata_wrong5, order_metadata_wrong6, order_metadata_wrong7, order_metadata_wrong8,
                 order_metadata_city, order_metadata_gender, order_metadata_province, order_metadata_company,
                 order_metadata_country, order_metadata_covid_no_symptoms, order_metadata_age, order_metadata_wrong9,
                 order_metadata_wrong10, order_metadata_wrong11, order_metadata_wrong12, order_metadata_wrong13,
                 order_metadata_wrong14, order_ticket_metadata_first_name, order_ticket_metadata_last_name,
                 order_ticket_wrong1, order_ticket_metadata_email, order_ticket_metadata_street,
                 order_ticket_metadata_street_number, order_ticket_metadata_street_number_additional,
                 order_ticket_metadata_postal, order_ticket_metadata_date_of_birth, order_ticket_metadata_state,
                 order_ticket_metadata_city, order_ticket_metadata_gender, order_ticket_metadata_province,
                 order_ticket_metadata_company, order_ticket_metadata_country, order_ticket_metadata_covid_no_symptoms,
                 order_ticket_metadata_age, order_ticket_wrong2, order_ticket_metadata_phone,
                 order_ticket_metadata_fullname, order_ticket_metadata_covid_one_household,
                 order_ticket_metadata_keep_me_informed, order_ticket_metadata_Diet, geolocation_street_name,
                 geolocation_street_number, geolocation_locality, geolocation_postal_code, geolocation_sub_locality,
                 geolocation_admin_level_1, geolocation_admin_level_2, geolocation_country_code, geolocation_latitude,
                 geolocation_longitude, ticket_pdf_link):
        self.order_id = order_id
        self.shop_name = shop_name
        self.event_name = event_name
        self.event_category = event_category
        self.first_event = first_event
        self.last_event = last_event
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.ticket_name = ticket_name
        self.barcode = barcode
        self.order_status = order_status
        self.order_invalidated = order_invalidated
        self.order_invalidated_at = order_invalidated_at
        self.ticket_invalidated = ticket_invalidated
        self.ticket_invalidated_at = ticket_invalidated_at
        self.created_at = created_at
        self.paid_currency = paid_currency
        self.order_value = order_value
        self.order_fees = order_fees
        self.transaction_fees = transaction_fees
        self.ticket_value = ticket_value
        self.ticket_fees = ticket_fees
        self.optionals_value = optionals_value
        self.refunded_amount = refunded_amount
        self.payment_method = payment_method
        self.coupons = coupons
        self.device = device
        self.tracker = tracker
        self.tracker_name = tracker_name
        self.seat = seat
        self.is_scanned = is_scanned
        self.first_scanned_at = first_scanned_at
        self.order_metadata_first_name = order_metadata_first_name
