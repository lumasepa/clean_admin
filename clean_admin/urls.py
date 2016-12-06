# -*- coding: utf-8 -*-
from django.conf.urls import url
from clean_admin.views import AdminActionsHistory


urlpatterns = [
    url(
        r'actions_history',
        AdminActionsHistory.as_view(),
        name='actions_history'
        ),
]
