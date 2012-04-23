# -*- coding: utf-8 -*-

def kotti_configure(settings):
    settings['kotti.includes'] += ' kotti_image_gallery.views'
    settings['kotti.available_types'] += ' kotti_image_gallery.resources.Gallery kotti_image_gallery.resources.Image'
