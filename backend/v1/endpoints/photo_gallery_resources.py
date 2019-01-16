from flask_restplus import Resource

from .. import photo_gallery_management_ns
from .data_model import DataModel
from .photo_gallery_service import PhotoGalleryService


@photo_gallery_management_ns.route('/v1/photo-galleries')
class PhotoGalleriesResource(Resource):

    @photo_gallery_management_ns.marshal_with(DataModel.PHOTO_GALLERY, envelope='data')
    def get(self):
        """
        Retrieve all photo galleries
        """
        return PhotoGalleryService.get_all(), 200
