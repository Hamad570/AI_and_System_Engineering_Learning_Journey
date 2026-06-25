from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import CandidateViewSet, cast_vote, index_view,blockchain_history

router = DefaultRouter()
router.register(r'candidates', CandidateViewSet, basename='candidate')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/vote/', cast_vote, name='cast_vote'),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('api/history/', blockchain_history, name='blockchain_history'),
    # Fallback to capture paths so frontend routing works seamlessly on reload
    re_path(r'^.*$', index_view, name='index'),
]