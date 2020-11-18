from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from login.models import Account
from login.serializers import AccountSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

@api_view(['POST'])
def login(request):
    """
    Get the username and password from the request.data and check whether correct.
    """
    if request.method == 'POST':
        # serializer = AccountSerializer(data=request.data)
        # if serializer.is_valid():
        data = JSONParser().parse(request)
        try:
            account = Account.objects.get(username=data['username'])
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if account.password != data['password']:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer = AccountSerializer(account)
                return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


