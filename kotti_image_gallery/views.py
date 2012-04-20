# -*- coding: utf-8 -*-

from kotti import DBSession
from kotti.views.edit import ContentSchema, generic_edit, generic_add
from kotti.views.util import ensure_view_selector
from kotti.views.view import view_node
from kotti_image_gallery.resources import Gallery, Image

class GallerySchema(ContentSchema):
    pass


class ImageSchema(ContentSchema):
    pass


@ensure_view_selector
def edit_gallery(context, request):
    return generic_edit(context, request, GallerySchema())

def add_gallery(context, request):
    return generic_add(context, request, GallerySchema(), Gallery, u'gallery')

@ensure_view_selector
def edit_image(context, request):
    return generic_edit(context, request, ImageSchema())

def add_image(context, request):
    return generic_add(context, request, ImageSchema(), Image, u'image')

def includeme_edit(config):

    config.add_view(edit_gallery,
                    context=Gallery,
                    name='edit',
                    permission='edit',
                    renderer='kotti:templates/edit/node.pt', )

    config.add_view(add_gallery,
                    name=Gallery.type_info.add_view,
                    permission='add',
                    renderer='kotti:templates/edit/node.pt', )

    config.add_view(edit_image,
                    context=Image,
                    name='edit',
                    permission='edit',
                    renderer='kotti:templates/edit/node.pt', )

    config.add_view(add_image,
                    name=Image.type_info.add_view,
                    permission='add',
                    renderer='kotti:templates/edit/node.pt', )

def view_gallery(context, request):

    session = DBSession()
    query = session.query(Image).filter(Image.parent_id==context.id)
    images = query.all()

    return {"images": images}


def includeme_view(config):
    config.add_view(view_gallery,
                    context=Gallery,
                    name='view',
                    permission='view',
                    renderer='templates/gallery-view.pt', )

    config.add_view(view_node,
                    context=Image,
                    name='view',
                    permission='view',
                    renderer='templates/image-view.pt', )

    config.add_static_view('static-kotti_image_gallery', 'kotti_image_gallery:static')

def includeme(config):
    includeme_edit(config)
    includeme_view(config)
