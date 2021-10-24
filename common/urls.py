"""
All Urls for the common app

"""


from django.urls import path

from common.views import CommonView


urlpatterns = [

    path("hello-world", CommonView.as_view()),

]


