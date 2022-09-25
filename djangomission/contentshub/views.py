from accounts.models import Master
from accounts.permissions import IsMasterUser
from contentshub.models import Klass, Comment
from contentshub.serializers import CommentSerializer, KlassCreateSerializer, KlassDetailSerializer, KlassListSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


# Create your views here.
class KlassCreateView(generics.CreateAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassCreateSerializer
    permission_classes = [IsAuthenticated&IsMasterUser]

    def post(self, request, *args, **kwargs):
        serializer = KlassCreateSerializer(data=request.data)

        if serializer.is_valid():
            klass = Klass.objects.create(
                writer = Master.objects.get(user=request.user),
                title = request.data['title'],
                content = request.data['content'],
            )
        
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KlassDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class KlassListView(generics.ListAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassListSerializer
    permission_classes = [AllowAny]


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            comment = Comment.objects.create(
                        user_id = request.user.id,
                        klass_id = self.kwargs['pk'],
                        content = request.data['content']
                    )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]