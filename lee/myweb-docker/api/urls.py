from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from api import views
from api.views import BlogViewSet, CategoryViewSet, TagViewSet

blog_list = BlogViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
blog_detail = BlogViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

category_list = CategoryViewSet.as_view({
    'get': 'list',
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
})

tag_list = TagViewSet.as_view({
    'get': 'list',
})

tag_detail = TagViewSet.as_view({
    'get': 'retrieve',
})

router = DefaultRouter()
router.register('blogs', views.BlogViewSet)
# router.register('category', views.CategorySerializer)
# router.register('tags', views.TagSerializer, base_name='tag')

urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/blogs/', blog_list, name='blog-list'),
    path('api/blogs/<int:pk>/', blog_detail, name='blog-detail'),
    path('api/categories/', category_list, name='category-list'),
    path('api/categories/<int:pk>/', category_detail, name='category-detail'),
    path('api/tags/', tag_list, name='tag-list'),
    path('api/tags/<int:pk>/', tag_detail, name='tag-detail'),
    path('api/', views.api_root)
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
