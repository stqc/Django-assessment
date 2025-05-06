from django.urls import path
from .views import TaskListAndCreateView, TaskDetailedView, RegisterView,swagger_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/', TaskListAndCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:id>/', TaskDetailedView.as_view(), name='task-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/',swagger_schema_view.with_ui('swagger'), name='swagger-schema'),
]