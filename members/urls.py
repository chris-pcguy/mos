from django.conf.urls import *
from django.views.generic.list import ListView

from mos.members.models import *

urlpatterns = patterns('',
    url(r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'members/member_login.html'}, name='login'),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', name='logout'),
    (r'^valid_user/?$', 'mos.members.views.valid_user',),

    (r'^$', ListView.as_view(queryset=get_active_members(), template_name='members/member_list.html')),
    (r'^history/$', 'mos.members.views.members_history'),
    url(r'^change_password/$', 'django.contrib.auth.views.password_change', {'template_name': 'members/member_update_password.html'}, name='password_change'),
    url(r'^change_password/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'members/member_update_password_done.html'}, name='password_change_done'),
    (r'^collection/$', 'mos.members.views.members_bankcollection_list'),
    (r'^keylist/$', 'mos.members.views.members_key_list'),
    (r'^lazzzorlist/$', 'mos.members.views.members_lazzzor_list'),
    (r'^scannerdoorlist/$', 'mos.members.views.members_sc8r_list'),
    (r'^(?P<user_username>(\w|-)+)/update/userpic/$', 'mos.members.views.members_update_userpic'),
    (r'^(?P<user_username>(\w|-)+)/update/(?P<update_type>\w+)/$', 'mos.members.views.members_update'),
    (r'^(?P<user_username>(\w|-)+)/$', 'mos.members.views.members_details'),
)
