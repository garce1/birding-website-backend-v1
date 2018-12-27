from flask_restplus import fields, Resource

from .. import photo_gallery_management_ns
from .photo_gallery_service import PhotoGalleryService

photo_gallery_model = photo_gallery_management_ns.model('photo-gallery', {
    'name': fields.String('Name of the photo gallery.')
})


@photo_gallery_management_ns.route('/v1/photo-galleries')
class PhotoGalleriesResource(Resource):

    @photo_gallery_management_ns.marshal_with(photo_gallery_model, envelope='data')
    def get(self):
        """
        retrieve all photo galleries
        """
        return PhotoGalleryService().get_all(), 200
