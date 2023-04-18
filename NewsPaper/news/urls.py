from django.urls import path
from .views import PostsList, PostDetail, subscriptions

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
