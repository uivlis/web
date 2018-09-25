# -*- coding: utf-8 -*-
"""Define the Account URLs.

Copyright (C) 2018 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
from django.urls import include, path, re_path

from rest_framework import routers

from . import api, views

app_name = 'account'

router = routers.DefaultRouter()
router.register(r'organization', api.OrganizationViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
    re_path(r'^orgs/view/(?P<org_name>\w+)/$', views.explorer_organzations, name='explorer_organzations'),
    path('orgs', views.organizations, name='organizations'),
    path('orgs/<int:org_handle>/follow', views.follow_organization, name='follow_org'),
    path('orgs/<int:org_handle>/unfollow', views.unfollow_organization, name='unfollow_org'),
)
