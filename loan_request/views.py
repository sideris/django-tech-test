from django.core.exceptions import ValidationError
from django.db import transaction
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from loan_request.models import Business, LoanRequest, Client


# in some utils package
class Messages:
    FORM_NOT_COMPLETE   = "Please fill all available fields"
    ERRONEOUS_DATA      = "There's something wrong with the data you have entered"
    REQUEST_SENT        = "Request has been received. You will be notified by email"

def make_message(message):
    return {'message': message}


class LoanRequestView(TemplateView):
    template_name = 'loan_request.html'

    def get_context_data(self, **kwargs):
        c = super(LoanRequestView, self).get_context_data(**kwargs)
        c['form_config'] = {
            'loan': {
                'amount_limit': list(LoanRequest.AMOUNT_LIMITS),
                'duration_limit': [1, 200]
            },
            'business': {
                'sectors': {item[0]: item[1] for item in Business.SECTORS}
            }
        }
        return c


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def test(request):
    return Response({"message": "Hello"})


@transaction.atomic
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def create_loan_request(request):
    data = request.data
    user_data = data.get('user', None)
    business_data = data.get('business', None)
    loan_request_data = data.get('loan_request', None)
    if None in [user_data, business_data, loan_request_data]:
        return Response(make_message(Messages.FORM_NOT_COMPLETE), status=status.HTTP_400_BAD_REQUEST)
    business = Business(**business_data)
    loan_request = LoanRequest(**loan_request_data)
    try:
        business.full_clean()
        loan_request.full_clean()
        business.save()
        loan_request.save()
        client = Client(business=business, request=loan_request, **user_data)
        client.full_clean()
        client.save()
    except ValidationError as ve:
        return Response(make_message(Messages.ERRONEOUS_DATA), status=status.HTTP_400_BAD_REQUEST)
    return Response(make_message(Messages.REQUEST_SENT))
