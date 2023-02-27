import datetime
import random
import string
from rest_framework.response import Response
from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.authtoken.admin import User
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from rest_framework import status
import pandas as pd
import ast


class postStudentDetailData(APIView):
    def post(self, request):
        data = request.data
        serializer = StudentDetailSerializer(data=data)
        if serializer.is_valid():

            studentId = 'student' + ''.join(
                random.choices(string.digits + string.ascii_letters, k=random.randint(5, 8)))

            StudentDetail.objects.create(
                studentId=studentId,
                **serializer.data

            )

            return Response({
                'status': 200,
                'message': "student Detail Create  Successfully"
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })

class getStudentDetail(APIView):
        def get(self, request):
            try:
                data = StudentDetail.objects.filter().values()

                return Response({
                    'status': 200,
                    'data': data
                })

            except Exception as e:
                return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'errors': str(e)
                })


class getStudentDetailId(APIView):
    def get(self, request,studentId):
        try:
            data = StudentDetail.objects.filter(studentId=studentId).values()

            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })

class postParentsDetail(APIView):
    def post(self, request):
        data = request.data
        serializer = parentsDetailSerializer(data=data)
        if serializer.is_valid():
            studentId = serializer.data["studentId"]
            parentsDetailData = serializer.data["parentsDetailData"]
            Address = serializer.data["Address"]

            parentsDetail.objects.create(
                studentId_id=studentId,
                parentsDetailData=parentsDetailData,
                Address=Address
            )

            return Response({
                'status': 200,
                'message': "Parents Detail Create  Successfully"
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })


class getParentsDetail(APIView):
        def get(self, request):
            try:
                data = parentsDetail.objects.filter().values()

                return Response({
                    'status': 200,
                    'data': data
                })

            except Exception as e:
                return Response({
                    'status': 400,
                    'message': 'Something went wrong',
                    'errors': str(e)
                })


class getParentsDetailId(APIView):
    def get(self, request,studentId_id):
        try:
            data = parentsDetail.objects.filter(studentId_id=studentId_id).values()

            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })
