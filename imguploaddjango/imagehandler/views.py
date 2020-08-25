from .models import Image
from .serializers import ImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ImageUp(APIView):
	"""
		create a new image.
	"""
	def get(self, request, format=None):
		images = Image.objects.all()
		serializer = ImageSerializer(images, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ImageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    	# data=request.data
    	# print(data)
    	# if request.method == 'POST' and request.FILES['image']:
	    #     myfile = request.FILES['image']
	    #     fs = FileSystemStorage()
	    #     filename = fs.save(myfile.name, myfile)
	    #     uploaded_file_url = fs.url(filename)
	    #     return Response({'msg' : 'worked'}, status=status.HTTP_200_OK)
    	# return Response({'msg' : 'not worked'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)