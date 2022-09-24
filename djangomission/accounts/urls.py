from django.urls import path, include
from accounts.views import IndividualOnlyView, IndividualSignupView, MasterOnlyView, MasterSignupView, CustomAuthToken, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('signup/individual', IndividualSignupView.as_view()),
    path('signup/master', MasterSignupView.as_view()),
    path('login', CustomAuthToken.as_view()),
    path('logout', LogoutView.as_view()),
    path('individual/dashboard', IndividualOnlyView.as_view()),
    path('master/dashboard', MasterOnlyView.as_view()),
 ] 