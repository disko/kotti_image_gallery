# -*- coding: utf-8 -*-

from kotti.resources import Content, File
from kotti.util import _
from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String, Unicode

class Gallery(Content):

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(name=u'Gallery',
                                       title=_(u'Gallery'),
                                       add_view=u'add_gallery',
                                       addable_to=[u'Document'], )


class Image(Content):

    id = Column(Integer(), ForeignKey('contents.id'), primary_key=True)
    data = Column(LargeBinary())
    filename = Column(Unicode(100))
    mimetype = Column(String(100))
    size = Column(Integer())

    type_info = File.type_info.copy(name=u'Image',
                                    title=_(u'Image'),
                                    add_view=u'add_image',
                                    addable_to=[u'Gallery'], )

    def __init__(self, data=None, filename=None, mimetype=None, size=None, **kwargs):

        super(File, self).__init__(**kwargs)

        self.data = data
        self.filename = filename
        self.mimetype = mimetype
        self.size = size
