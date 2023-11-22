from django.urls import path,include
from .views import SignUpView


urlpatterns = [
    path('user/signup/', SignUpView.as_view()),
    path('user/', include('dj_rest_auth.urls'))
]