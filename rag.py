from sentence_transformers import SentenceTransformer
from mongo import collection


# Set model config
MODEL_NAME = "all-MiniLM-L6-v2"
MODEL_DIMENSIONS = 384

# initialize model for making embeddings
model = SentenceTransformer(MODEL_NAME, trust_remote_code=True)


# function to generate embeddings
def get_embedding(problem):
    """Generates vector embeddings for the given data."""

    embedding = model.encode(problem)
    return embedding.tolist()


# function to add text, embeddings
def insert_problem(problem):
    embedding = get_embedding(problem=problem)
    collection.insert_one(
        {
            "text": problem,
            "embedding": embedding,
        }
    )


# function to run vector search queries
def get_query_results(query):
    print("Records fetching")
    """Gets results from a vector search query."""

    query_embedding = get_embedding(query)
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "exact": True,
                "limit": 5,
            }
        },
        {"$project": {"_id": 0, "text": 1}},
    ]

    results = collection.aggregate(pipeline)

    array_of_results = []
    for doc in results:
        array_of_results.append(doc)
    return array_of_results
