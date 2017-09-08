from django.conf.urls import url

from .import views

app_name='frontend'

urlpatterns=[
    url(r'^orderstatus/$',views.status,name='status'),
    url(r'^search/$',views.search,name='search'),
    url(r'^items/(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^items/(?P<item_id>[0-9]+)/req/$', views.req, name='request'),
    url(r'^items/$',views.items,name='items'),
    url(r'^$',views.index,name='index'),
    url(r'^login/$', views.signin, name='signin'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^update/$', views.update, name='update'),
    url(r'^logout/$', views.logout_user, name='logout'),
]