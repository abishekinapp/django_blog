


from django.conf.urls import url
from posts import views  # the '.' means it will serch in the project folder and fid out the file

urlpatterns =[

    url(r'^$',views.post_list,name ='home'),

]
