from flask_restplus.fields import List, Nested, String

from .. import image_management_ns, photo_gallery_management_ns


class DataModel:

    IMAGE_METADATA = image_management_ns.model('ImageMetadata', {
        'category': String(description='Category [BIRDS, HERPETO, INSECTS, LANDSCAPER, MAMMALS]', required=True),
        'descriptionEnglish': String(description='Description in English'),
        'descriptionPortuguese': String(description='Description in Portuguese'),
        'location': String(description='Where is the picture from?'),
        'sourceFileName': String(description='Source file name', required=True),
        'speciesNameEnglish': String(description='Specie\'s English name'),
        'speciesNameLatin': String(description='Specie\'s Latin name'),
        'speciesNamePortuguese': String(description='Specie\'s Portuguese name'),
        'tags': List(String, description='Tags used to classify, group, or find the image', unique=True),
    })

    IMAGE = image_management_ns.model('Image', {
        'id': String(description='Image UUID'),
        'metadata': Nested(IMAGE_METADATA),
        'url': String(description='URL for public access'),
    })

    IMAGE_CREATE_REQUEST = image_management_ns.model('ImageCreateRequest', {
        'metadata': Nested(IMAGE_METADATA, allow_null=False, required=True),
    })

    IMAGE_CREATE_RESPONSE = image_management_ns.model('ImageCreateResponse', {
        'uploadUrl': String(description='Temporary URL to upload the content'),
    })

    PHOTO_GALLERY = photo_gallery_management_ns.model('PhotoGallery', {
        'name': String(description='Name of the photo gallery', required=True),
    })

