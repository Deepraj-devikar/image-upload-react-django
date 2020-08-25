from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Check(APIView):
    """
    create a new user.
    """
    def post(self, request, format=None):
    	data=request.data
    	print(data)
    	return Response({'msg' : 'worked'}, status=status.HTTP_200_OK)