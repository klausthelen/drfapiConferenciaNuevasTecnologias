from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [	
url(r'^', include('rest_auth.urls')),
url(r'^register/', include('rest_auth.registration.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)