from .api import ApiV1

photo_gallery_management_ns = None


def setup_api(app):
    api_v1 = ApiV1(app)

    global photo_gallery_management_ns
    photo_gallery_management_ns = api_v1.namespace('photo-gallery-mgmt', description='Photo gallery management')

    from .endpoints import PhotoGalleriesResource
