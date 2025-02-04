from pymongo.operations import SearchIndexModel
from mongo import collection
from rag import MODEL_DIMENSIONS


# Create your index model, then create the search index
index_name = "vector_index"
search_index_model = SearchIndexModel(
    definition={
        "fields": [
            {
                "type": "vector",
                "numDimensions": MODEL_DIMENSIONS,
                "path": "embedding",
                "similarity": "cosine",
            }
        ]
    },
    name=index_name,
    type="vectorSearch",
)
collection.create_search_index(model=search_index_model)
