from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response

class UserMixin(object):

        valid_user = None

        def dispatch(self, request, *args, **kwargs):
            try:
                user, token = TokenAuthentication().authenticate(request)
                self.valid_user = user
            except:
                return JsonResponse({"status": 
                                        "Authentication credentials were not provided."}, 
                                                                status=status.HTTP_401_UNAUTHORIZED)
            return super().dispatch(request, *args, **kwargs)

class TodoListCreate(UserMixin, ListCreateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

	def get_queryset(self):
		return Todo.objects.filter(user=self.valid_user)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.validated_data['user'] = self.valid_user
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, 
										headers=headers, 
											status=status.HTTP_201_CREATED) 

class TodoRetrieveUpdateDelete(UserMixin, RetrieveUpdateDestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

