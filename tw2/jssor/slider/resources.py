# -*- coding: utf-8 -*-
#
# tw2.jssor.slider - a jssor slider widget
#
# Copyright © 2014 - 2016 Nils Philippsen <nils@tiptoe.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from __future__ import unicode_literals, absolute_import

import pkg_resources
pkg_resources.require("tw2.core >= 2.0")

from tw2.core import JSLink, DirLink


jssor_slider_js = JSLink(
    modname=__name__, filename="static/js/jssor.slider.min.js")

# Other resources

static_resources = DirLink(modname=__name__, filename="static")
