from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.permissions import IsOwnerOrReadOnly
from api.serializer import BlogSerializer, CategorySerializer, TagSerializer
from blog.models import Blog, Category, Tag


# from rest_framework import status
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework import mixins
# from rest_framework import generics


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'blogs': reverse('blog-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'tags': reverse('tag-list', request=request, format=format)
    })


# class BlogList(APIView):
#     """
#     列出所有的snippets或者创建一个新的snippet。
#     """
#     def get(self, request, format=None):
#         snippets = Blog.objects.all()
#         serializer = BlogSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class BlogList(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供`list`和`detail`操作。
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    此视图自动提供`list`和`detail`操作。
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    此视图自动提供`list`和`detail`操作。
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
