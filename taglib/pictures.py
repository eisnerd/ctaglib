from taglib import *

class Picture(object):
    mapping = {
        'data': taglib_picture_data,
        'mimetype': taglib_picture_mimetype,
        'description': taglib_picture_description,
        'typename': taglib_picture_typename,
        'typecode': taglib_picture_typecode,
    }
    def __init__(self, picture):
        self.picture = picture

    def __getattribute__(self, attr):
        try:
            f = Picture.mapping[attr]
        except Exception, error:
            return super(Picture, self).__getattribute__(attr)
        return f(self.picture)

def pictures(file):
    ps = taglib_file_pictures(file)
    while True:
        picture = taglib_pictures_next(ps)
        if picture:
            yield Picture(picture)
        else:
            break