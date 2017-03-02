import json

import pytest

from loan_request.views import Messages, make_message

person = {
    "name": "Test",
    "email": "test@test.com",
    "telephone": "0044 0790000000"
}
business = {
    "name": "Test Business",
    "sector": 0,
    "address": "Some address",
    "registered_number": 1234567890
}
loan_request = {
    "amount": 10000,
    "duration": 200,
    "description": "some reason"
}


def get_payload(p, b, lr):
    return {
        "user": p,
        "business": b,
        "loan_request": lr
    }


@pytest.mark.django_db()
def test_loan_endpoint(client):
    from loan_request.models import Client

    url = '/api/loan/'

    # success state
    result = client.post(url, json.dumps(get_payload(person, business, loan_request)),
                         content_type="application/json")
    assert result.status_code == 200
    assert json.loads(result.content) == make_message(Messages.REQUEST_SENT)
    client_entry = Client.objects.filter(name=person['name']).first()
    assert client_entry is not None
    client_data = client_entry.json()
    for k, v in person.iteritems():
        assert v == client_data[k]
    for k, v in business.iteritems():
        if k != 'sector':
            assert v == client_data['business'][k]
        else:
            assert v == client_data['business'][k]['value']
    for k, v in loan_request.iteritems():
        assert v == client_data['request'][k]
    # Error states
    erroneous_payload = get_payload(person, business, {})
    result = client.post(url, json.dumps(erroneous_payload),
                         content_type="application/json")
    assert result.status_code == 400
    assert json.loads(result.content) == make_message(Messages.ERRONEOUS_DATA)

    erroneous_payload.pop('loan_request')
    result = client.post(url, json.dumps(erroneous_payload),
                         content_type="application/json")
    assert result.status_code == 400
    assert json.loads(result.content) == make_message(Messages.FORM_NOT_COMPLETE)

    result = client.get(url)
    assert result.status_code == 405  # method not allowed
