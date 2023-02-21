from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import *
# Create your views here.



def home(request):
    return render(request ,'home.html')


def download(request , uid):
    return render(request , 'download.html' , context = {'uid' : uid})


class HandelFileUpload(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request): 
        try:
            data = request.data
            srlr= FileListSerializer(data=data)

            if data: 

                if srlr.is_valid():
                    srlr.save()
                    return Response({
                        'staus': 200,
                        'message': 'files uploaded successfully',
                        'data': srlr.data
                    })

                return Response({
                    'status' : 400,
                    'message' : 'somethign went wrong',
                    'data'  : srlr.errors
                })

            return Response({
                'status' : 401,
                'message' : 'no data upload',
            })

        except Exception as e:
            print(e)
