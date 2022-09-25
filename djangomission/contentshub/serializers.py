from accounts.models import User
from contentshub.models import Klass, Comment
from rest_framework import serializers

class KlassCreateSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Klass
        fields = ['title', 'writer', 'content'] 


class KlassListSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='user.username')
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Klass
        fields = ['id', 'title', 'writer', 'content','comment_count']

    def get_comment_count(self, obj):
        comment = Comment.objects.filter(klass_id=obj.id)
        comment_count = {
                'comment_count' : len(comment)
                }
        return comment_count


class KlassDetailSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='user.username')
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Klass
        fields = ['id', 'title', 'writer', 'content', 'comment']

    def get_comment(self, obj):
        comment = [{
            'user'      :User.objects.get(id=comment.user_id).username,
            'content'   :comment.content,
        } for comment in Comment.objects.filter(klass_id=obj.id)]
        return comment
    

class CommentSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='user.username')
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['writer', 'content']
        read_only_fields = ['writer']

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data