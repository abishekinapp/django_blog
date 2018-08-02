
from django.conf.urls import url
from home.views import HomeView
from home import views


urlpatterns =[

    url(r'^$',HomeView.as_view(),name ='home'),
    #url(r'^<int:pk>/',views.post_detail, name='post_detail'),
    url(r'^postlist/',views.postlist,name ='postlist'),
    url(r'post_detail/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    url(r'add_comment/(?P<pk>\d+)/', views.add_comment, name='add_comment'),
]
