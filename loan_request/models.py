from __future__ import unicode_literals

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db.models import Model, CharField, IntegerField, BooleanField, CASCADE, OneToOneField


class LoanRequest(Model):
    AMOUNT_LIMITS = (10000, 100000)
    amount      = IntegerField(null=False, validators=[MinValueValidator(AMOUNT_LIMITS[0]),
                                                       MaxValueValidator(AMOUNT_LIMITS[1])])
    duration    = IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(365)])
    approved    = BooleanField(null=False, default=False)
    description = CharField(null=False, max_length=1000)

    def json(self):
        return {
            'amount': self.amount,
            'duration': self.duration,
            'description': self.description
        }


class Business(Model):
    # this should come from a site-config.json or similar
    SECTORS = ((0, 'Retail'), (1, 'Professional Services'), (2, 'Food & Drink'), (3, 'Entertainment'))

    name                = CharField(null=False, max_length=300)
    sector              = IntegerField(null=False, choices=SECTORS, default=0)
    address             = CharField(null=False, max_length=200)
    registered_number   = IntegerField(null=False, validators=[RegexValidator(r'^\d{10,10}$')])

    def json(self):
        return {
            'name': self.name,
            'sector': {'name': self.get_sector_display(), 'value': self.sector},
            'address': self.address,
            'registered_number': self.registered_number
        }


class Client(Model):
    name        = CharField(null=False, max_length=100)
    email       = CharField(null=False, max_length=200)
    telephone   = CharField(null=False, max_length=15)
    request     = OneToOneField(LoanRequest, on_delete=CASCADE, related_name='client')
    business    = OneToOneField(Business, on_delete=CASCADE, related_name='client')

    def json(self):
        return {
            'name': self.name,
            'email': self.email,
            'telephone': self.telephone,
            'request': self.request.json() if hasattr(self, 'request') else None,
            'business': self.business.json() if hasattr(self, 'business') else None,
        }
