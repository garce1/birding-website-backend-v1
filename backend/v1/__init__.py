from .api import ApiV1

image_management_ns = None
photo_gallery_management_ns = None


def setup_api(app):
    api_v1 = ApiV1(app)

    global image_management_ns
    image_management_ns = api_v1.namespace('image-mgmt', description='Image management')

    global photo_gallery_management_ns
    photo_gallery_management_ns = api_v1.namespace('photo-gallery-mgmt', description='Photo gallery management')

    from .endpoints import ImagesResource
    from .endpoints import PhotoGalleriesResource
