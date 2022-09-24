# Create your views here.
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer, IndividualSignupSerializer, MasterSignupSerializer
from accounts.permissions import IsIndividualUser, IsMasterUser


class IndividualSignupView(generics.GenericAPIView):
    serializer_class = IndividualSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user' : UserSerializer(user, context=self.get_serializer_context()).data,
            'token' : Token.objects.get(user=user).key,
            'message' : 'account created successfully!'
        })


class MasterSignupView(generics.GenericAPIView):
    serializer_class = MasterSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user' : UserSerializer(user, context=self.get_serializer_context()).data,
            'token' : Token.objects.get(user=user).key,
            'message' : 'account created successfully!'
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token' : token.key,
            'user_id' : user.pk,
            'is_master' : user.is_master
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class IndividualOnlyView(generics.RetrieveAPIView):
    permission_classes =  [permissions.IsAuthenticated&IsIndividualUser]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user


class MasterOnlyView(generics.RetrieveAPIView):
    permission_classes =  [permissions.IsAuthenticated&IsMasterUser]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user