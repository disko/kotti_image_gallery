===================
kotti_image_gallery
===================

This is an extension to the Kotti CMS that allows you to add galleries
with images to your Kotti site.

It uses the `Bootstrap Image Gallery`_.

`Find out more about Kotti`_

.. _Bootstrap Image Gallery: https://github.com/blueimp/Bootstrap-Image-Gallery
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To activate the kotti_image_gallery add-on in your Kotti site,
you need to add an entry to the ``kotti.configurators`` setting in
your Paste Deploy config.  If you don't have a ``kotti.configurators``
option, add one.  The line in your ``[app:main]`` section could then
look like this::

  kotti.configurators = kotti_image_gallery.kotti_configure

With this, you'll be able to add gallery and image items in your site.
