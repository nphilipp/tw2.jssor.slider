# -*- coding: utf-8 -*-
#
# tw2.jssor.slider - a jssor slider widget
#
# Copyright © 2014, 2015 Nils Philippsen <nils@tiptoe.de>
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

from __future__ import unicode_literals, print_function, absolute_import

import pkg_resources
pkg_resources.require("tw2.core >= 2.0")
pkg_resources.require("tw2.jquery >= 2.0")

from tw2.core import Widget, JSLink, CSSLink, Link, Param, Variable
from tw2.core import JSSource
from tw2.jquery.base import jquery_js, jQuery
from tw2.jquery.version import JSLinkMixin

__all__ = (
    "jssor_slider_js", "JssorBulletNavigator", "JssorSlider")

# JS Links

jssor_slider_js = JSLink(
    modname=__name__, filename="static/js/jssor.slider.min.js")

# Other resources

static_resources = Link(modname=__name__, filename="static", whole_dir=True)

# Widgets

class JssorBulletNavigator(Widget):

    template = 'genshi:tw2.jssor.slider.templates.bulletnavigator'

    opacity = Param("bullet opacity", default=0.7)

    cursor = Param("cursor type", default='pointer')

    normcolor = Param("color (normal)", default='gray')
    activecolor = Param("color (active)", default='#fff')
    mouseovercolor = Param("color (mouseover)", default='#d3d3d3')
    mousedowncolor = Param("color (mousedown)", default='#555555')

    bullet_width = Param("width of the bullet", default="12px")
    bullet_height = Param("height of the bullet", default="12px")

    horizontal_position = Param(
            "horizontal position (left, center, right)",
            default='center')
    horizontal_gap = Param("horizontal gap to border", default="16px")

    vertical_position = Param(
            "vertical position (top, center, bottom)",
            default='bottom')
    vertical_gap = Param("vertical gap to border", default="16px")

    spacing = Param("spacing between bullets", default="10px")

    _opacity_percent = Variable("computed opacity in percent")
    _horpos = Variable("computed style to set horizontal position")
    _vertpos = Variable("computed style to set vertical position")

    _center_style_tmpl = "{pos1}: 50%; margin-{pos2}: -50%; " + "; ".join(
            "{what}transform: translate{{XY}}(-50%)".format(
                what=what) for what in (
                    "", "-webkit-", "-ms-", "-o-", "-moz-"))

    _hor_center_style = _center_style_tmpl.format(
            pos1="left", pos2="right", XY="X")

    _vert_center_style = _center_style_tmpl.format(
            pos1="top", pos2="bottom", XY="Y")

    def prepare(self):
        super(JssorBulletNavigator, self).prepare()

        self._opacity_percent = int(self.opacity * 100)

        if self.horizontal_position == 'center':
            self._horpos = self._hor_center_style
        else:
            self._horpos = "{pos}: {gap}".format(
                    pos=self.horizontal_position, gap=self.horizontal_gap)

        if self.vertical_position == 'center':
            self._vertpos = self._vert_center_style
        else:
            self._vertpos = "{pos}: {gap}".format(
                    pos=self.vertical_position, gap=self.vertical_gap)

class JssorSlider(Widget):

    template = None

    resources = [jquery_js, jssor_slider_js]

    container = Param("id of the slider container")

    responsive = Param(
            "whether the slider should react to resizing etc.", default=False)

    options = Param(
        "(dict) of Jssor Slider options", default={})

    _responsive_tmpl = """    function ScaleSlider() {{
        var parentWidth = $('#{container}').parent().width();
        if (parentWidth) {{
            jssor_slider1.$ScaleWidth(parentWidth);
        }}
        else
            window.setTimeout(ScaleSlider, 30);
    }}

    ScaleSlider();

    $(window).on('load', ScaleSlider);
    $(window).on('resize', ScaleSlider);
    $(window).on('orientationchange', ScaleSlider);"""

    _js_tmpl_begin = """jQuery(document).ready(function ($) {{
    var options = {options};
    var jssor_slider1 = new $JssorSlider$('{container}', options);
"""

    _js_tmpl_end = "}});"

    _js_tmpl_nonresponsive = _js_tmpl_begin + _js_tmpl_end
    _js_tmpl_responsive = _js_tmpl_begin + _responsive_tmpl + _js_tmpl_end

    def dict_to_js(self, options_dict):
        options_strs = []
        for k, v in options_dict.items():
            if isinstance(v, dict):
                v_str = self.dict_to_js(v)
            elif isinstance(v, bool):
                v_str = "true" if v else "false"
            else:
                v_str = str(v)
            options_strs.append("{k}:{v}".format(k=k, v=v_str))
        return r"{{{options}}}".format(options=",".join(options_strs))

    def prepare(self):
        super(JssorSlider, self).prepare()

        if self.responsive:
            js_tmpl = self._js_tmpl_responsive
        else:
            js_tmpl = self._js_tmpl_nonresponsive

        js_source = JSSource(src=js_tmpl.format(
            options=self.dict_to_js(self.options),
            container=self.container))

        self.resources.append(js_source)

    def generate_output(self, displays_on):
        return u""
