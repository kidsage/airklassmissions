from accounts.models import User, Master
from community.models import Comment
from contentshub.models import Klass
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
        fields = ['title', 'writer', 'content','comment_count']

    def get_comment_count(self, obj):
        comment = Comment.objects.filter(klass_id=obj.id)
        comment_count = {
                'comment_count' : len(comment)
                }
        return comment_count


class KlassDetailSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='user.username')
    comment = serializers.SerializerMethodField()

    def get_comment(self, obj):
        comment = [{
            'user'      :User.objects.get(id=comment.user_id).username,
            'content'   :comment.content,
        } for comment in Comment.objects.filter(klass_id=obj.id)]
        return comment

    class Meta:
        model = Klass
        fields = ['title', 'writer', 'content', 'comment']