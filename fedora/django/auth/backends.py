# -*- coding: utf-8 -*-
#
# Copyright © 2009  Ignacio Vazquez-Abrams All rights reserved.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.  You should have
# received a copy of the GNU General Public License along with this program;
# if not, write to the Free Software Foundation, Inc., 51 Franklin Street,
# Fifth Floor, Boston, MA 02110-1301, USA. Any Red Hat trademarks that are
# incorporated in the source code or documentation are not subject to the GNU
# General Public License and may only be used or replicated with the express
# permission of Red Hat, Inc.
#
'''
.. moduleauthor:: Ignacio Vazquez-Abrams <ivazquez@fedoraproject.org>
'''
from fedora.django import connection
from fedora.django.auth.models import FasUser

from django.db.models.signals import post_syncdb

class FasBackend:
    def authenticate(self, username=None, password=None):
        if connection.verify_password(username, password):
            userinfo = connection.person_by_username(username)
            user = FasUser.objects.user_from_fas(userinfo)
            if user.is_active:
                return user

    def get_user(self, userid):
        userinfo = connection.person_by_id(userid)
        return FasUser.objects.user_from_fas(userinfo)