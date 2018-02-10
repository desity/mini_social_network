from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf.urls import url
from starnavi.views import *
from starnavi.views_api import *

urlpatterns = [
    url(r'^$', index, name='post_list'),
    url(r'^api/$', PostList.as_view()),
    url(r'^api/userposts/$', UserPosts.as_view()),
    url(r'^api/register/$', Registration.as_view()),
    url(r'^api/post/(?P<pk>[0-9]+)/addlike/$', PostLikeDislike.as_view()),
    url(r'^api/api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
