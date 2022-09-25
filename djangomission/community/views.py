from multiprocessing import AuthenticationError
from accounts.permissions import IsIndividualUser, IsMasterUser
from community.models import Question,Answer
from community.serializers import QuestionSerializer, AnswerSerializer, QuestionListSerializer, QuestionDetailSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            question = Question.objects.create(
                klass_id = self.kwargs['pk'],
                writer = self.request.user,
                content = request.data['content'],
            )

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionListVIew(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    permission_classes = [AllowAny]


class QuestionDetailVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        question = Question.objects.filter(id=self.kwargs['pk'])
        answer = Answer.objects.filter(question_id=self.kwargs['pk']).first()

        if answer == None:
            self.perform_destroy(question)
            return Response("delete question successfully!", status=status.HTTP_200_OK)

        elif answer != None and answer.writer.is_individual == True:
            return Response("do not delete question. because exist answer.", status=status.HTTP_401_UNAUTHORIZED)

        elif answer != None and answer.writer.is_master == True:
            self.perform_destroy(question)
            return Response("delete question successfully!", status=status.HTTP_200_OK)
        


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = AnswerSerializer(data=request.data)

        if serializer.is_valid():
            answer = Answer.objects.create(
                question_id = self.kwargs['pk'],
                writer = self.request.user,
                content = request.data['content'],
            )

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetailVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]