from rest_framework import serializers

from blog.models import Blog, Category, Tag


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.ReadOnlyField(source='category.name')
    tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'excerpt', 'content', 'category',
                  'tag', 'author', 'create_time', 'image_static',
                  'image_url', 'image_author')
        # fields = '__all__'
        # depth = 1
        # read_only_fields = ('account_name',)


#
class CategorySerializer(serializers.ModelSerializer):
    blog = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='blog-detail'
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'blog')


class TagSerializer(serializers.ModelSerializer):
    blog = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='blog-detail'
    )

    class Meta:
        model = Tag
        fields = ('id', 'name', 'blog')
