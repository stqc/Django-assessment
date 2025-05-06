from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema



class TaskListAndCreateView(APIView):

    @swagger_auto_schema(
        operation_description="Get tasks for authenticated user, with optional ?is_completed filter",
        responses={200: TaskSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter('is_completed', openapi.IN_QUERY, description="Filter by completion status", type=openapi.TYPE_BOOLEAN, required=False)
        ]
    )
    
    def get(self, request):

        tasks = Task.objects.filter(owner=request.user)

        if request.query_params.get('is_completed') is not None:
            is_completed = request.query_params.get('is_completed')
            tasks = Task.objects.filter(owner=request.user, is_completed=is_completed.lower() == 'true')
            
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=TaskSerializer,
        responses={201: TaskSerializer}
    )

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class TaskDetailedView(APIView):
    @swagger_auto_schema(responses={200: TaskSerializer, 404: "Task not found"}
                         )
    def get(self,request,id):
        try:
            task = Task.objects.get(id=id, owner=request.user)
        except Task.DoesNotExist:
            return Response(status=404)
        
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=TaskSerializer, responses={200: TaskSerializer, 404: "Task not found"})
    
    def patch(self,request,id):
        try:
            task = Task.objects.get(id=id, owner=request.user)
        except Task.DoesNotExist:
            return Response(status=404)
        
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    

class RegisterView(APIView):
    
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={201: "User created successfully", 400: "Username already exists"}
    )

    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)
        
        User.objects.create_user(username=username, password=password)

        return Response({"message": "User created successfully"}, status=201)
    
swagger_schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="API for managing tasks",
        ),
        public=True,
        permission_classes=[AllowAny],
       )