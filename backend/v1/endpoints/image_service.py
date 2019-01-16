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
        metadata_dict = image['metadata']
        metadata.update({
            'category': metadata_dict['category'],
            'descriptionEnglish': metadata_dict['descriptionEnglish'],
            'descriptionPortuguese': metadata_dict['descriptionPortuguese'],
            'location': metadata_dict['location'],
            'sourceFileName': metadata_dict['sourceFileName'],
            'speciesNameEnglish': metadata_dict['speciesNameEnglish'],
            'speciesNameLatin': metadata_dict['speciesNameLatin'],
            'speciesNamePortuguese': metadata_dict['speciesNamePortuguese'],
            'tags': metadata_dict['tags'],
        })
        client.put(metadata)
        return metadata

    @staticmethod
    def __validate_image_data_before_save(image):
        assert image['metadata'], 'metadata must be provided'
        assert image['metadata']['category'], 'metadata.category must be provided'
        assert image['metadata']['sourceFileName'], 'metadata.sourceFileName must be provided'
