# -*- coding: utf-8 -*-

import PIL
from kotti import DBSession
from kotti.util import _
from kotti.views.edit import ContentSchema, make_generic_add, make_generic_edit
from kotti.views.file import AddFileFormView, EditFileFormView
from kotti_image_gallery import image_scales
from kotti_image_gallery.resources import Gallery, Image
from plone.scale.scale import scaleImage
from pyramid.response import Response
from pyramid.view import view_config

PIL.ImageFile.MAXBLOCK = 33554432

class GallerySchema(ContentSchema):
    pass


class BaseView(object):

    def __init__(self, context, request):

        self.context = context
        self.request = request


class GalleryView(BaseView):

    @view_config(context=Gallery,
                 name='view',
                 permission='view',
                 renderer='templates/gallery-view.pt')
    def view(self):

        session = DBSession()
        query = session.query(Image).filter(Image.parent_id==self.context.id).order_by(Image.position)
        images = query.all()

        return {"images": images}


class EditImageFormView(EditFileFormView):

    pass


class AddImageFormView(AddFileFormView):

    item_type = _(u"Image")

    def add(self, **appstruct):

        buf = appstruct['file']['fp'].read()

        return Image(title=appstruct['title'],
                     description=appstruct['description'],
                     data=buf,
                     filename=appstruct['file']['filename'],
                     mimetype=appstruct['file']['mimetype'],
                     size=len(buf), )


class ImageView(BaseView):

    @view_config(context=Image,
                 name='view',
                 permission='view',
                 renderer='templates/image-view.pt')
    def view(self):
        return {}

    @view_config(context=Image,
                 name="image",
                 permission='view')
    def image(self):
        """return the image in a specific scale, either inline (default) or as attachment"""

        subpath = list(self.request.subpath)

        if (len(subpath) > 0) and (subpath[-1] == "download"):
            disposition = "attachment"
            subpath.pop()
        else:
            disposition = "inline"

        if len(subpath) == 1:
            scale = subpath[0]
            if scale in image_scales:
                # /path/to/image/scale/thumb
                width, height = image_scales[scale]
            else:
                # /path/to/image/scale/160x120
                try:
                    width, height = [int(v) for v in scale.split("x")]
                except ValueError:
                    width, height = (None, None)

        elif len(subpath) == 2:
            # /path/to/image/scale/160/120
            try:
                width, height = [int(v) for v in subpath]
            except ValueError:
                width, height = (None, None)

        else:
            # don't scale at all
            width, height = (None, None)

        if width and height:
            image, format, size = scaleImage(self.context.data,
                                             width=width,
                                             height=height,
                                             direction="thumb")
        else:
            image = self.context.data

        res = Response(
            headerlist=[('Content-Disposition', '%s;filename="%s"' % (disposition,
                                                                      self.context.filename.encode('ascii', 'ignore'))),
                        ('Content-Length', str(len(image))),
                        ('Content-Type', str(self.context.mimetype)), ],
            app_iter=image)

        return res

def includeme(config):

    config.add_static_view('static-kotti_image_gallery', 'kotti_image_gallery:static')
    config.scan("kotti_image_gallery")
    config.add_view(AddImageFormView,
                    name=Image.type_info.add_view,
                    permission='add',
                    renderer='kotti:templates/edit/node.pt',)
    config.add_view(EditImageFormView,
                    context=Image,
                    name='edit',
                    permission='edit',
                    renderer='kotti:templates/edit/node.pt', )

    config.add_view(make_generic_edit(GallerySchema()),
                    context=Gallery,
                    name='edit',
                    permission='edit',
                    renderer='kotti:templates/edit/node.pt', )

    config.add_view(make_generic_add(GallerySchema(), Gallery),
                    name=Gallery.type_info.add_view,
                    permission='add',
                    renderer='kotti:templates/edit/node.pt', )
