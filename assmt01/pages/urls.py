from django.urls import path
from django.conf.urls.static import static  # test
from .views import HomePageView, PostPageView, PostsPageViewList, CreatePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/", PostPageView.as_view(), name="post"),  # new
    path("posts/", PostsPageViewList.as_view(), name="posts"),  # new
    path("create/", CreatePageView.as_view(), name="create"),  # new
]
