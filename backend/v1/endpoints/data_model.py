from flask_restplus.fields import Nested
from flask_restplus.fields import String

from .. import image_management_ns
from .. import photo_gallery_management_ns


class DataModel:

    IMAGE_CREATE_RESPONSE = image_management_ns.model('image-create-response', {
    })

    IMAGE_METADATA = image_management_ns.model('image-metadata', {
        'category': String(description='Category [birds, herpeto, insects, landscapes, mammals]', required=True),
        'description-english': String(description='Description in English'),
        'description-portuguese': String(description='Description in Portuguese'),
        'location': String(description='Where is the picture from?'),
        'source-file-name': String(description='Source file name', required=True),
        'species-name-english': String(description='Specie\'s English name'),
        'species-name-latin': String(description='Specie\'s Latin name'),
        'species-name-portuguese': String(description='Specie\'s Portuguese name'),
        'tags': String(description='Image\'s tags'),
    })

    IMAGE = image_management_ns.model('image', {
        'id': String(description='Image UUID'),
        'metadata': Nested(IMAGE_METADATA, allow_null=False, required=True),
        'url': String(description='URL for public access'),
    })

    PHOTO_GALLERY = photo_gallery_management_ns.model('photo-gallery', {
        'name': String(description='Name of the photo gallery', required=True)
    })

