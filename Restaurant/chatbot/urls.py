from django.urls import path
from .views import chatbot_response
from . import views

urlpatterns = [
    path('chat-form/', views.chat_view, name='chat'),
    path("chat/", chatbot_response, name="chatbot_response"),
] 