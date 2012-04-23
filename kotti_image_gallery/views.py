# -*- coding: utf-8 -*-

from colander import null, SchemaNode
from deform import FileData
from deform.widget import FileUploadWidget
from kotti import DBSession
from kotti.util import _
from kotti.views.edit import ContentSchema, generic_edit, generic_add
from kotti.views.file import FileUploadTempStore, attachment_view, inline_view
from kotti.views.util import ensure_view_selector
from kotti_image_gallery.resources import Gallery, Image
from pyramid.view import view_config


class GallerySchema(ContentSchema):
    pass



class BaseView(object):

    def __init__(self, context, request):

        self.context = context
        self.request = request


class GalleryView(BaseView):

    @view_config(name=Gallery.type_info.add_view,
                 permission='add',
                 renderer='kotti:templates/edit/node.pt')
    def add(self):

        return generic_add(self.context,
                           self.request,
                           GallerySchema(),
                           Gallery,
                           u'gallery')

    @ensure_view_selector
    @view_config(context=Gallery,
                 name='edit',
                 permission='edit',
                 renderer='kotti:templates/edit/node.pt')
    def edit(self):

        return generic_edit(self.context,
                            self.request,
                            GallerySchema())

    @view_config(context=Gallery,
                 name='view',
                 permission='view',
                 renderer='templates/gallery-view.pt')
    def view(self):

        session = DBSession()
        query = session.query(Image).filter(Image.parent_id==self.context.id)
        images = query.all()

        return {"images": images}


class ImageView(BaseView):

    def schema_factory(self):

        tmpstore = FileUploadTempStore(self.request)

        class ImageSchema(ContentSchema):
            file = SchemaNode(FileData(),
                              title=_(u'File'),
                              missing=null,
                              widget=FileUploadWidget(tmpstore), )

        return ImageSchema()

    @view_config(name=Image.type_info.add_view,
                 permission='add',
                 renderer='kotti:templates/edit/node.pt')
    def add(self):
        return generic_add(self.context,
                           self.request,
                           self.schema_factory(),
                           Image,
                           u'image')

    @ensure_view_selector
    @view_config(context=Image,
                 name='edit',
                 permission='edit',
                 renderer='kotti:templates/edit/node.pt')
    def edit(self):

        return generic_edit(self.context,
                            self.request,
                            self.schema_factory())

    @view_config(context=Image,
                 name='view',
                 permission='view',
                 renderer='templates/image-view.pt')
    def view(self):
        return {}

    @view_config(context=Image,
                 name="image",
                 permission='view')
    def inline_view(self):
        return inline_view(self.context, self.request)

    @view_config(context=Image,
                 name="image_download",
                 permission='view')
    def attachment_view(self):
        return attachment_view(self.context, self.request)

def includeme(config):

    config.add_static_view('static-kotti_image_gallery', 'kotti_image_gallery:static')
    config.scan("kotti_image_gallery")
