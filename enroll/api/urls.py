from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()
router.register('student', views.SnippetViewSet, basename='student')
router.register('user', views.UserViewSet, basename='user')


urlpatterns = [
    path('api/', include(router.urls)),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    
    path('api-auth/', include('rest_framework.urls')),
]


# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns

# # API endpoints
# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#     path('snippets/',
#         views.StudentList.as_view({'get': 'list'}),
#         name='snippet-list'),
#     path('snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])
