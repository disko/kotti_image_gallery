# -*- coding: utf-8 -*-

from kotti.resources import Content, File
from kotti.util import _
from sqlalchemy import Column, ForeignKey, Integer

class Gallery(Content):

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(name=u'Gallery',
                                       title=_(u'Gallery'),
                                       add_view=u'add_gallery',
                                       addable_to=[u'Document'], )


class Image(File):

    id = Column(Integer(), ForeignKey('files.id'), primary_key=True)

    type_info = File.type_info.copy(name=u'Image',
                                    title=_(u'Image'),
                                    add_view=u'add_image',
                                    addable_to=[u'Gallery'], )
