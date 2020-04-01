from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from floors import views as floor_views
from profiles import views as profile_views
from config import views as config_views

router = DefaultRouter()
router.register(r'project', floor_views.ProjectViewSet)
router.register(r'ScopeOfWorkViewSet', floor_views.ScopeOfWorkViewSet)
router.register(r'ContactPersonViewSet', floor_views.ContactPersonViewSet)
router.register(r'ContactDataViewSet', floor_views.ContactDataViewSet)
router.register(r'ProjectCommentViewSet', floor_views.ProjectCommentViewSet)

router.register(r'user', profile_views.UserViewSet)
router.register(r'CurrentUser', profile_views.CurrentUserViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('giupulloriginmaster/', config_views.giupulloriginmaster),
]
