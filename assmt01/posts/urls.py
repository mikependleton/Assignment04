from django.urls import path
from .views import PostPageView
urlpatterns = [

    path("post/", PostPageView.as_view(), name="post"),  # new

]
