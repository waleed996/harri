"""
All Urls for the common app

"""


from django.urls import path

from common.views import CommonView


urlpatterns = [

    # Basic Hello World Test API
    path("hello-world", CommonView.as_view()),

]


