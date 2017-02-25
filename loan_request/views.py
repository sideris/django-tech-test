from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def test(request):
    return Response({"message": "Hello"})