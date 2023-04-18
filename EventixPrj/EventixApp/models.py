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
