from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .. import views

# Créez un routeur
router = DefaultRouter()

# Enregistrez vos ViewSets
router.register(r'candidates', views.CandidateViewSet, basename='candidate')
router.register(r'recruiters', views.RecruiterViewSet, basename='recruiter')
router.register(r'jobposts', views.JobPostViewSet, basename='jobpost')

# Ajoutez les URL générées par le routeur
urlpatterns = [
    path('api/', include(router.urls)),
]
