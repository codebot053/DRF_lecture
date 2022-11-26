from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post',views.PostViewSet) # 2개의 URL을 만들어준다.
                                          # 만들어진 두개의 URL패턴은 router.urls에 있다.

urlpatterns = [
    path('',include(router.urls)),
    path("list/",views.PostListApiView.as_view()),
]