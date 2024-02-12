from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from rembg import remove
from PIL import Image


class RemoveBgView(ListAPIView):
    
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        try:
            input_path = request.data['image']
            input = Image.open(input_path)
            output = remove(input)
            output.convert('RGB')
            output_path = 'media/'+str(input_path.name).split(".")[0]+".png"
            output.save(output_path)
            print("Image processed and saved successfully")
            return Response(output_path, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error processing image: {e}")
            return Response(f"Error processing image: {e}", status=status.HTTP_502_BAD_GATEWAY)