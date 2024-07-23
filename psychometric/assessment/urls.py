from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssessmentViewSet, QuestionViewSet, ResponseViewSet

router = DefaultRouter()
router.register(r'assessments', AssessmentViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
