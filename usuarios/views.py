from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# from .models import UserManage
# from .serializers import UserManageSerilizer
#
#
# class UserManageViewSet(viewsets.ModelViewSet):
#     queryset = UserManage.objects.all()
#     serializer_class = UserManageSerilizer
