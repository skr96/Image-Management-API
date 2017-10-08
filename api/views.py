import os
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from PIL import Image
from rest_framework import status
import uuid

def index(request):
    return HttpResponse("<h1> This is the home page </h1>")


class image_list(APIView):
    """
        View to list upload, list and delete all images for the user.
        * Requires token authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # Signature : Response(data, status=None, template_name=None, headers=None, content_type=None)

    def get(self, request):
        username = request.user.username
        user_dir = os.path.join(settings.IMAGE_DIR, username)
        img_list = os.listdir(user_dir)
        lst = []
        for i, image in enumerate(img_list):
            lst.append({"image_" + str(i): image})
        if not lst:
            lst.append({"message": "No image found"})
        return Response(lst)

    def post(self, request):
        if 'image' in request.FILES:
            img = request.FILES['image']
            try:
                ig = Image.open(img)    #PIL library to check if file uploaded is image
            except IOError:
                output = {
                    "message": "Uploaded file not a valid image"
                }
                return Response(output, status=status.HTTP_400_BAD_REQUEST)
            width, height = ig.size
            size = width * height
            if size > settings.MAX_UPLOAD_SIZE:
                output = {
                    "message": "Max upload size exceeded. Try another image."
                }
                return Response(output, status=status.HTTP_400_BAD_REQUEST)

            else:
                username = request.user.username
                user_dir = os.path.join(settings.IMAGE_DIR, username)
                print user_dir
                image_name = img.name
                print image_name
                image_path = os.path.join(user_dir,image_name)
                if os.path.isfile(image_path):        # to check if file with this name already exists
                    img_name,ext=image_name.split(".")
                    img_name+= str(uuid.uuid4().hex)
                    image_name=img_name+'.'+ext
                    print image_name
                image_path = os.path.join(user_dir, image_name)
                ig.save(image_path,quality=70)      # quality>95 is known to increase size in certain cases.
                output = {
                    'image_name': image_name,
                }
                return Response(output, status=status.HTTP_201_CREATED)
        else:
            output = {
                "message": "No file uploaded"
            }
            return Response(output, status=status.HTTP_400_BAD_REQUEST)


class image_detail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, image):
        username = request.user.username
        user_dir = os.path.join(settings.IMAGE_DIR, username)
        image_path = os.path.join(user_dir, image)
        if os.path.isfile(image_path):
            image = open(image_path, "rb").read()
            return Response(image, status= status.HTTP_200_OK, content_type="image/*")
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, image):
        if 'image' in request.FILES:
            img = request.FILES['image']
            try:
                ig = Image.open(img)    #PIL library to check if file uploaded is image
            except IOError:
                output = {
                    "message": "Uploaded file not a valid image"
                }
                return Response(output, status=status.HTTP_400_BAD_REQUEST)
            width, height = ig.size
            size = width * height
            if size > settings.MAX_UPLOAD_SIZE:
                output = {
                    "message": "Max upload size exceeded. Try another image."
                }
                return Response(output, status=status.HTTP_400_BAD_REQUEST)
            else:
                username = request.user.username
                user_dir = os.path.join(settings.IMAGE_DIR, username)
                image_path = os.path.join(user_dir,image)
                if os.path.isfile(image_path):
                    os.remove(image_path)
                    ig.save(image_path,quality=70)      # quality>95 is known to increase size in certain cases.
                    output = {
                        'message' : 'Image successfully updated. '
                    }
                    return Response(output, status=status.HTTP_201_CREATED)
                else:
                    output = {
                        "message": "File does not exist."
                    }
                    return Response(output, status=status.HTTP_400_BAD_REQUEST)
        else:
            output = {
                "message": "No file uploaded"
            }
            return Response(output, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, image):
        username = request.user.username
        user_dir = os.path.join(settings.IMAGE_DIR, username)
        image_path = os.path.join(user_dir,image)
        if os.path.isfile(image_path):
            os.remove(image_path)
            output = {
                "message": "File successfully deleted. "
            }
            return Response(output, status=status.HTTP_200_OK)
        else:
            output = {
                "message": "File does not exist. "
            }
            return Response(output, status=status.HTTP_404_NOT_FOUND)