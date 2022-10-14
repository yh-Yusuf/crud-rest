from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *

@api_view(['POST' , 'GET' , 'PATCH'])
def home(request):
    if request.method =='GET':
         return Response(
             {   'status':200,
                 'message': 'success GET method'
             }
         )
    elif request.method =='POST':
         return Response(
             {   'status':200,
                 'message': 'success POST method'
             }
         )
    elif request.method =='PATCH':
         return Response(
             {   'status':200,
                 'message': 'success PATCH method'
             }
         )
    else:
         return Response(
             {   'status':200,
                 'message': 'invalid method'
             }
         )

@api_view(['GET'])
def get_model(request):
    post_objs = post.objects.all()
    serializer = post_serializer(post_objs , many= True)

    return Response({
        "status" : True,
        "message": "post fetched",
        "data" : serializer.data
    })

@api_view(['DELETE'])
def delete_all(request):
    post_objs = post.objects.all().delete()
    serializer = post_serializer(post_objs, many=True)

    return Response({
        "status" : True,
        "message": "posts deleted",
        # "data" : serializer.data
    })




@api_view(['POST'])
def post_model(request):
    try:
        data = request.data
        serializer = post_serializer(data = data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(
                {
                    "status": True,
                    "message":"success post created",
                    "data": serializer.data
                }
            )
        return Response(
            {
                "status": False,
                "message": "Invalid data",
                "data": serializer.data
            }
        )

    except Exception as e:
        print(e)
    return Response(
        {
            "status": False,
            "message": "soemthing went wrong",

        }
    )


@api_view(['GET'])
def single_post(request, id):
    post_obj = post.objects.get(id=id)
    if post_obj:
        serializer = post_serializer(post_obj)
        return Response(serializer.data)
    else:
        return Response(data={"message": "Error"})


@api_view(['DELETE'])
def delete_post(request, idx):
    post_obj = post.objects.get(id=idx)

    if post_obj:
        post_obj.delete()
        return Response(data={"message": "Deleted Successfully"})
    else:
        return Response(date={"message": "Found Nothing to Delete"})


@api_view(['PUT'])
def update_post(request, id):
    post_obj = post.objects.get(id=id)
    if post_obj:
        data = request.data
        serializer = post_serializer(instance=post_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
    else:
        return Response(date={"message": "Data Not Found"})
