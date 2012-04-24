# -*- coding: utf-8 -*-

from kotti.testing import UnitTestBase

class SettingsTests(UnitTestBase):

    def test_01_defaults(self):

        settings = {'kotti.includes': '',
                    'kotti.available_types': '', }

        import kotti_image_gallery

        kotti_image_gallery.kotti_configure(settings)

        self.assertTrue(settings['kotti.includes'].find('kotti_image_gallery.views') >= 0)
        self.assertTrue(settings['kotti.available_types'].find('kotti_image_gallery.resources.Gallery') >= 0)
        self.assertTrue(settings['kotti.available_types'].find('kotti_image_gallery.resources.Image') >= 0)

        self.assertEquals(kotti_image_gallery.image_scales['thumb'], [160, 120])
        self.assertEquals(kotti_image_gallery.image_scales['carousel'], [560, 420])

    def test_02_override_defaults(self):

        settings = {'kotti.includes': '',
                    'kotti.available_types': '',
                    'kotti_image_gallery.scale_thumb' : '100x200',
                    'kotti_image_gallery.scale_carousel' : '300x400', }

        import kotti_image_gallery

        kotti_image_gallery.kotti_configure(settings)

        self.assertEquals(kotti_image_gallery.image_scales['thumb'], [100, 200])
        self.assertEquals(kotti_image_gallery.image_scales['carousel'], [300, 400])

    def test_03_additional_scale(self):

        settings = {'kotti.includes': '',
                    'kotti.available_types': '',
                    'kotti_image_gallery.scale_huge' : '1000x2000', }

        import kotti_image_gallery

        kotti_image_gallery.kotti_configure(settings)

        self.assertEquals(kotti_image_gallery.image_scales['huge'], [1000, 2000])

    def test_04_ivalid_scale(self):

        settings = {'kotti.includes': '',
                    'kotti.available_types': '',
                    'kotti_image_gallery.scale_invalid' : '100,200', }

        import kotti_image_gallery

        kotti_image_gallery.kotti_configure(settings)

        self.assertTrue('invalid' not in kotti_image_gallery.image_scales)
