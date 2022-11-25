from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from movies.models import *


@registry.register_document
class MovieDocument(Document):
    class Index:
        name = "movie"

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = Movie
        fields = ["id", "title"]
