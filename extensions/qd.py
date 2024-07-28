from django.apps import apps
from tqdm import tqdm

from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
load_dotenv()
# Initialize QdrantClient and Sentence Transformer
client = QdrantClient(
    url=os.getenv(
        "QDRANT_URL"
    ), 
    api_key=os.getenv(
        "QDRANT_API_KEY"
    ),
)
model_transformer = SentenceTransformer('all-MiniLM-L6-v2')

# Get all models in the 'products' app
all_models = apps.get_app_config('products').get_models()

for Model in all_models:
    # Use model name to define the collection name
    collection_name = Model._meta.model_name.lower()

    # Recreate collection for the current model
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=384,
            distance=models.Distance.COSINE
        )
    )

    # Fetch all instances of the model
    items = Model.objects.all()

    # Process each item
    for item in tqdm(items, desc=f"Processing {Model._meta.model_name}"):
        # Assume there's a 'name' field to encode, adjust if different
        if hasattr(item, 'name'):
            vector = model_transformer.encode(item.name)

            # Construct payload, check for attributes and adjust accordingly
            payload = {
                "name": item.name if hasattr(item, 'name') else "No name",
                "price": item.actual_price if hasattr(item, 'actual_price') else 0,
                "image": item.image if hasattr(item, 'image') else None,
                "main_category": item.main_category if hasattr(item, 'main_category') else "No category",
                "sub_category": item.sub_category if hasattr(item, 'sub_category') else "No subcategory"
            }

            # Upsert into Qdrant
            client.upsert(
                collection_name=collection_name,
                points=[
                    models.PointStruct(
                        id=item.id,
                        vector=vector,
                        payload=payload
                    )
                ]
            )

