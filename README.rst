===================
kotti_image_gallery
===================

This is an extension to the Kotti CMS that allows you to add galleries with images to your Kotti site.

It uses `Bootstrap Carousel`_ for the gallery view.

`Find out more about Kotti`_


Setup
=====

To activate the ``kotti_image_gallery`` add-on in your Kotti site, you need to add an entry to the ``kotti.configurators`` setting in your Paste Deploy config.
If you don't have a ``kotti.configurators`` option, add one.
The line in your ``[app:main]`` section could then look like this::

  kotti.configurators = kotti_image_gallery.kotti_configure

With this, you'll be able to add gallery and image items in your site.


Image URLs
==========

``kotti_image_gallery`` provides on-the-fly image scaling by utilizing `plone.scale`_ (thanks to Tom Lazar for the hint).

Images (including arbitrary scales) can be referenced by this URL schema: ``/path/to/image_content_object/image[[/<image_scale>]/download]`` where ``<image_scale>`` can be:

 - a predefined image scale (see below)
 - a string of the form ``<max_width>x<max_height>`` or
 - a URL path segment of the form ``<max_width>/<max_height>``

If the last URL path segment is ``download``, the image will be served with ``Content-disposition: attachment`` otherwise it will be served with ``Content-disposition: inline``.

Predefined image scale sizes
----------------------------

You may define image scale sizes in your ``.ini`` file by setting values for ``kotti_image_gallery.scale_<scale_name>`` to values of the form ``<max_width>x<max_height>`` (e.g. ``kotti_image_gallery.scale_thumb = 160x120`` with the resulting scale name ``thumb``).

``thumb`` (160x120) and ``carousel`` (560x420) are always defined (because they are used in the default templates), but their values can be overwritten by setting ``kotti_image_gallery.scale_thumb`` and/or ``kotti_image_gallery.scale_carousel`` to different values in your .ini file.


Work in progress
================

``kotti_image_gallery`` is considered alpha software, not suitable for use in production environments.
The current state of the project is in no way feature complete nor API stable.
If you really want to use it in your project(s), make sure to pin the exact version in your requirements.
Not doing so will likely break your project when future releases become available.


Development
===========

Contributions to ``kotti_image_gallery`` are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

Note that all development is done on the ``develop`` branch and ``master`` is reserved for "production-ready state".
Therefore make sure to always base your work on the current state of the ``develop`` branch.

This follows the highly recommended `A successful Git branching model`_ pattern, which is implemented by the excellent `gitflow`_ git extension.

Testing
-------

``kotti_image_gallery`` has 100% test coverage.
Please make sure that you add tests for new features and that all tests pass before submitting pull requests.
Running the test suite is as easy as running ``py.test`` from the source directory.


.. _Bootstrap Carousel: http://twitter.github.com/bootstrap/javascript.html#carousel
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _`plone.scale`: http://pypi.python.org/pypi/plone.scale/1.2.2
.. _Github repository: https://github.com/disko/kotti_image_gallery
.. _gitflow: https://github.com/nvie/gitflow
.. _A successful Git branching model: http://nvie.com/posts/a-successful-git-branching-model/
