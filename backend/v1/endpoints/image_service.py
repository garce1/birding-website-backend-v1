import datetime

from google.cloud import datastore


class ImageService:

    __ENTITY_IMAGE_EXCLUDE_FROM_INDEXES = ('url',)
    __ENTITY_METADATA_EXCLUDE_FROM_INDEXES = ('descriptionEnglish', 'descriptionPortuguese', 'location',
                                              'sourceFileName', 'tags',)

    @staticmethod
    def save(image):
        ImageService.__validate_image_data_before_save(image)

        # TODO Save to Cloud Datastore
        client = datastore.Client()
        image = ImageService.__persist_image(client, ImageService.__persist_metadata(client, image))

        # TODO Generate Cloud Storage Signed URL and return
        return image

    @staticmethod
    def __persist_image(client, metadata):
        key = client.key('Image')
        image = datastore.Entity(key, exclude_from_indexes=ImageService.__ENTITY_IMAGE_EXCLUDE_FROM_INDEXES)
        image.update({
            'created': datetime.datetime.utcnow(),
            'metadata': metadata,
            'url': key.id,
        })
        client.put(image)
        return image

    @staticmethod
    def __persist_metadata(client, image):
        key = client.key('ImageMetadata')
        metadata = datastore.Entity(key, exclude_from_indexes=ImageService.__ENTITY_METADATA_EXCLUDE_FROM_INDEXES)
        metadata.update({
            'category': image['metadata']['category'],
            'descriptionEnglish': image['metadata']['descriptionEnglish'],
            'descriptionPortuguese': image['metadata']['descriptionPortuguese'],
            'location': image['metadata']['location'],
            'sourceFileName': image['metadata']['sourceFileName'],
            'speciesNameEnglish': image['metadata']['speciesNameEnglish'],
            'speciesNameLatin': image['metadata']['speciesNameLatin'],
            'speciesNamePortuguese': image['metadata']['speciesNamePortuguese'],
            'tags': image['metadata']['tags'],
        })
        client.put(metadata)
        return metadata

    @staticmethod
    def __validate_image_data_before_save(image):
        assert image['metadata'], 'metadata must be provided'
        assert image['metadata']['category'], 'metadata.category must be provided'
        assert image['metadata']['sourceFileName'], 'metadata.sourceFileName must be provided'
