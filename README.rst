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


Image scales
============

``kotti_image_gallery`` doesn't provide image scaling itself (yet?).
To have a visually appealing gallery view with the default `Bootstrap Carousel`_ based template, it is required to have the same height for all images in the gallery (at least within the gallery view itself).
To not rely on the different browsers' image scaling capabilities (and save bandwith by serving scaled images instead of the maybe huge originals), the included ``development.ini`` sets up a WSGI pipeline with a `repoze.bitblt`_ filter.
To adjust the height of the carousel you just need to set the ``height`` attribute of the ``img`` tag in ``gallery-view.pt`` to the desired value.
This might become configurable by the content manager in future releases.


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

This follows the highly recommended `A successful Git branching model`_ pattern, which is backed the the excellent `gitflow`_ git extension.


.. _Bootstrap Carousel: http://twitter.github.com/bootstrap/javascript.html#carousel
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _repoze.bitblt: http://pypi.python.org/pypi/repoze.bitblt
.. _Github repository: https://github.com/disko/kotti_image_gallery
.. _gitflow: https://github.com/nvie/gitflow
.. _A successful Git branching model: http://nvie.com/posts/a-successful-git-branching-model/
