# -*- coding: utf-8 -*-

# default image scales
image_scales = {
    'thumb': [160, 120],
    'carousel': [560, 420]}

import logging
log = logging.getLogger(__name__)

def kotti_configure(settings):

    settings['kotti.includes'] += ' kotti_image_gallery.views'
    settings['kotti.available_types'] += ' kotti_image_gallery.resources.Gallery kotti_image_gallery.resources.Image'

    for k in settings.keys():
        if k.startswith("kotti_image_gallery.scale_"):
            try:
                x, y = [int(v) for v in settings[k].split("x")]
            except ValueError:
                log.error("Invalid value for %s: '%s' (image scales must be <width>x<height>. e.g. 200x100")
            else:
                image_scales[k[26:]] = [x, y]
