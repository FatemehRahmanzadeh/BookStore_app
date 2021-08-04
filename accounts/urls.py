# با اضاف شدن
# allauth
# نیای به این فایل نیست

from django.urls import path
from .views import SignupPageView
urlpatterns = [
path('signup/', SignupPageView.as_view(), name='signup'),
]