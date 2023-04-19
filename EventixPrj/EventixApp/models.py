from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

# User#


class User(models.Model):
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
    id = models.AutoField
    secret = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    updated_at = models.CharField(max_length=100)


# Cards #


class Wrap(models.Model):
    id = models.AutoField
    account = models.ForeignKey(User, on_delete=models.CASCADE)


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    wrap = models.ForeignKey(Wrap, on_delete=models.CASCADE)
    context = models.JSONField(default=list)


# Transaction #
class Transaction(models.Model):
    oder_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    event_category = models.CharField
    event_subcategory = models.CharField
    first_event = models.CharField
    last_event = models.CharField
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    ticket_name = models.CharField(max_length=255)
    barcode = models.CharField
    order_status = models.CharField(max_length=15)
    order_invalidated = None
    order_invalidated_at = None
    ticket_invalidated = None
    ticket_invalidated_at = None
    created_at = models.CharField
    paid_currency = models.FloatField
    order_value = models.FloatField
    order_fees = models.FloatField
    transaction_fees = models.FloatField
    ticket_value = models.FloatField
    ticket_fees = models.FloatField
    optionals_value = models.FloatField
    refunded_amount = models.FloatField
    payment_id = None
    payment_method = None
    coupons = None
    device = models.CharField(max_length=15)
    tracker = None
    tracker_name = None
    seat = None
    is_scanned = models.BooleanField
    first_scanned_at = models.CharField
    order_metadata_first_name = None
    order_metadata_last_name = None
    order_metadata_wrong1 = None
    order_metadata_wrong2 = None
    order_metadata_wrong3 = None
    order_metadata_wrong4 = None
    order_metadata_wrong5 = None
    order_metadata_wrong6 = None
    order_metadata_wrong7 = None
    order_metadata_wrong8 = None
    order_metadata_city = models.CharField(max_length=15)
    order_metadata_gender = models.CharField
    order_metadata_province = models.CharField
    order_metadata_company = None
    order_metadata_country = models.CharField
    order_metadata_covid_no_symptoms = None
    order_metadata_age = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(120)]
    )
    order_metadata_wrong9 = None
    order_metadata_wrong10 = None
    order_metadata_wrong11 = None
    order_metadata_wrong12 = None
    order_metadata_wrong13 = None
    order_metadata_wrong14 = None
    order_ticket_metadata_first_name = None
    order_ticket_metadata_last_name = None
    order_ticket_wrong1 = None
    order_ticket_metadata_email = None
    order_ticket_metadata_street = None
    order_ticket_metadata_street_number = None
    order_ticket_metadata_street_number_additional = None
    order_ticket_metadata_postal = None
    order_ticket_metadata_date_of_birth = None
    order_ticket_metadata_state = None
    order_ticket_metadata_city = None
    order_ticket_metadata_gender = None
    order_ticket_metadata_province = None
    order_ticket_metadata_company = None
    order_ticket_metadata_country = None
    order_ticket_metadata_covid_no_symptoms = None
    order_ticket_metadata_age = None
    order_ticket_wrong2 = None
    order_ticket_metadata_phone = None
    order_ticket_metadata_fullname = None
    order_ticket_metadata_covid_one_household = None
    order_ticket_metadata_keep_me_informed = None
    order_ticket_metadata_Diet = None
    geolocation_street_name = None
    geolocation_street_number = None
    geolocation_locality = None
    geolocation_postal_code = None
    geolocation_sub_locality = None
    geolocation_admin_level_1 = None
    geolocation_admin_level_2 = None
    geolocation_country_code = None
    geolocation_latitude = None
    geolocation_longitude = None
    ticket_pdf_link = None
