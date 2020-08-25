from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ImageUp(APIView):
    """
    create a new image.
    """
    def post(self, request, format=None):
    	data=request.data
    	print(data)
    	return Response({'msg' : 'worked'}, status=status.HTTP_200_OK)