from __future__ import absolute_import, unicode_literals
from .widgets import JssorSlider
from .widgets import JssorBulletNavigator
from .resources import static_resources


class DemoJssorSlider(JssorSlider):

    template = None

    resources = JssorSlider.resources + [static_resources]

    container = 'slider_container'

    responsive = False

    options = {
       '$AutoPlay': True,
       '$SlideShowOptions': {
           '$Class': '$JssorSlideshowRunner$',
           '$Transitions': [{'$Fade': True, '$Duration': 1200, '$Opacity': 2}],
           '$TransitionsOrder': 1,
           '$ShowLink': True
       },
       #'$BulletNavigatorOptions': {
       #    '$Class': "$JssorBulletNavigator$",
       #    '$ChanceToShow': 1,
       #    '$SpacingX': 10,
       #}
    }


    def generate_output(self, displays_on):
        static = static_resources.req()
        static.prepare()

        img_div = """        <div>
            <img data-u="img" src="{static.link}/img/landscape/{imgno:02}.jpg" alt="" />
        </div>"""

        img_divs = "\n".join(img_div.format(static=static, imgno=i+1)
                             for i in range(12))

        output_tmpl = """<div id="slider_container"
    style="position: relative; top: 0px; left: 0px; width: 400px; height: 300px;">
    <div data-u="slides" style="cursor: move; position: absolute;
                                overflow: hidden; left: 0px; top: 0px;
                                width: 400px; height: 300px;">
{img_divs}
    </div>
</div>"""

        return output_tmpl.format(img_divs=img_divs)

class DemoJssorBulletNavigator(JssorBulletNavigator):
    pass
