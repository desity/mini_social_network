import datetime
from starnavi.serializers import StarnaviSerializer, Like_UnlikeSerializer, RegistrationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import status, serializers
from datetime import datetime
from .auth_up_in import *
from starnavi.models import Post, Like_Unlike
from django.contrib.auth.models import User
from .clearbit import clearbit_def
from .emailhunter import verify_email




#API
class Registration(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        deliver(request.data['email'])
        if verify_email(request.data['email']):
            raise serializers.ValidationError('This email is gibberish')
        k = clearbit_def(request.data['email'])
        if k != None:
            request.data['first_name'] = k.split(' ')[0]
            request.data['last_name'] = k.split(' ')[1]
        #erialized = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(APIView):
    #permission_classes = (IsAuthenticatedOrReadOnly)

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = StarnaviSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StarnaviSerializer(data=request.data)
        request.data['author_id'] = User.objects.get(username=request.user.username).pk
        request.data['like'] = 0
        request.data['dislike'] = 0
        request.data['created_date'] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPosts(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        posts = Post.objects.filter(author_id=User.objects.get(username=request.user.username).pk)
        serializer = StarnaviSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StarnaviSerializer(data=request.data)
        request.data['author_id'] = User.objects.get(username=request.user.username).pk
        request.data['like'] = 0
        request.data['dislike'] = 0
        request.data['created_date'] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostLikeDislike(APIView):
    #permission_classes = (IsAuthenticated)

    def get(self, request, pk, format=None):
        lds = Like_Unlike.objects.filter(login_id=User.objects.get(username=request.user.username).pk, post_id=pk)
        serializer = Like_UnlikeSerializer(lds, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        serializer = Like_UnlikeSerializer(data=request.data)
        request.data['post_id'] = pk
        request.data['login_id'] = User.objects.get(username=request.user.username).pk
        request.data['created_date'] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
        if serializer.is_valid():
            serializer.save()
            t = Post.objects.get(pk=pk)
            t.like = Like_Unlike.objects.filter(value=True, post_id=pk).count()
            t.dislike = Like_Unlike.objects.filter(value=False, post_id=pk).count()
            t.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class PostLikeDislike(APIView):
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = StarnaviSerializer
#     permission_classes = (IsAuthenticated,)
#     #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#
# class LikeUnlikelist(generics.ListCreateAPIView):
#      queryset = Like_Unlike.objects.all()
#      serializer_class = Like_UnlikeSerializer
#      permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = StarnaviSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsOwnerOrReadOnly,)

# class LikeUnlikelist(generics.ListCreateAPIView):
#     queryset = Like_Unlike.objects.all()
#     serializer_class = Like_UnlikeSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)