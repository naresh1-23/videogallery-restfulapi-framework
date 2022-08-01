import os
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import GallerySerializer
from .models import Gallery
from moviepy.editor import VideoFileClip
from django.core.files.storage import FileSystemStorage

# Post the video
@api_view(['POST'])
def home(request):
    try:
        data = request.data
        serializer = GallerySerializer(data = data)
        if serializer.is_valid():
            video = serializer.data['video']
            vid = VideoFileClip(video)
            vid_duration = int(vid.duration)
            if vid_duration<60:
                return Response({
                    'status': False,
                    'message':'length should be less than 60 second'
                })
            serializer.save()
            return Response({
                'status': True,
                'message': 'video uploaded',
                'data': serializer.data
            })
        else:
            return Response({
                'status': False,
                'message': 'invalid data',
                'data': serializer.errors
            })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'something went wrong'
    })



#Get all the video uploaded
@api_view(['GET'])
def get_video(request):
    video_obj = Gallery.objects.all()
    serializer = GallerySerializer(video_obj, many = True)
    return Response({
        'status': True,
        'message': 'here is the uploaded video',
        'data': serializer.data
    })


    
# Create your views here.
