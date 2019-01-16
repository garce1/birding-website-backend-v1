from flask_restplus import abort, Resource

from .. import image_management_ns
from .data_model import DataModel
from .image_service import ImageService


@image_management_ns.route('/v1/images')
class ImagesResource(Resource):

    @image_management_ns.expect(DataModel.IMAGE_CREATE_REQUEST)
    @image_management_ns.marshal_with(DataModel.IMAGE_CREATE_RESPONSE, code=201, description='Created')
    def post(self):
        """
        Stores data for a new image

        Returns a temporary URL that must be used within 2 minutes to upload image's content.
        """
        try:
            return ImageService.save(image_management_ns.payload), 201
        except AssertionError as e:
            raise abort(400, e.args[0])

    @image_management_ns.errorhandler(KeyError)
    def handle_key_exception(self):
        """
        Return a custom message and 400 status code
        """
        return {'message': '{} {}'.format(
            'Please verify the payload and make sure all fields are present.',
            'Non required fields must be present, but may contain null values')}, 400
