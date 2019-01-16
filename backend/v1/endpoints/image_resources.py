from flask_restplus import Resource

from .. import image_management_ns
from .data_model import DataModel
from .image_service import ImageService


@image_management_ns.route('/v1/images')
class ImagesResource(Resource):

    @image_management_ns.marshal_with(DataModel.IMAGE_CREATE_RESPONSE)
    def post(self):
        """
        Stores data for a new image
        Returns a temporary url that must be used within 2 minutes to upload the media itself.
        """
        return ImageService.save(), 201
