from django.urls import path

from wsv.views import GetMetadata

urlpatterns = [
    path('<str:iswc>/', GetMetadata.as_view()),
]
