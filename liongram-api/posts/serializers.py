from rest_framework.serializers import ModelSerializer

from .models import Post

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  
        #fields = ['id', 'writer', 'content', ]


class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = ['id', 'writer', 'content', ]
        depth = 1

class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = ['image', 'content', ]

class PostDeleteModelSerializer(PostBaseModelSerializer):
    pass


