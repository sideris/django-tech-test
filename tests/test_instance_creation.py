import mock
import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from loan_request.models import Business, LoanRequest, Client


def make_business(sector, registration):
    return Business(name="test",
                    address="Some address",
                    sector=sector,
                    registered_number=registration)


def make_loan_request(amount, duration):
    return LoanRequest(amount=amount, duration=duration,
                       description="Some test description")


def make_client():
    return Client(name="John Doe", email="some.email@email.com",
                  telephone="0044 07012345678")


def test_business_model():
    good_registration_number = 1234567890
    bad_registration_number = 123
    good_sector_value = 1
    bad_sector_value = 20
    with pytest.raises(ValidationError) as verror:
        make_business(good_sector_value, bad_registration_number).full_clean()
        make_business(bad_sector_value, good_registration_number).full_clean()
    make_business(good_sector_value, good_registration_number).full_clean()


def test_request_model():
    good_amount = 10000
    bad_amount_1 = 100
    bad_amount_2 = 1000000
    good_duration = 200
    bad_duration = 19999
    with pytest.raises(ValidationError) as verror:
        make_loan_request(bad_amount_1, good_duration).full_clean()
        make_loan_request(bad_amount_2, good_duration).full_clean()
        make_loan_request(good_amount, bad_duration).full_clean()
    make_loan_request(good_amount, good_duration).full_clean()


@pytest.mark.django_db(transaction=True)
def test_client_model():
    business = make_business(1, 1234567890)
    business.save()
    loan_request = make_loan_request(10000, 200)
    loan_request.save()

    client = make_client()
    assert client.json()['request'] is None
    assert client.json()['business'] is None
    with pytest.raises(IntegrityError) as ierror:
        client.save()
    client.request = loan_request
    client.business = business
    assert client.json()['request'] is not None
    assert client.json()['business'] is not None
    client.save()