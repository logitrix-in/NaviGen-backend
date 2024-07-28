from products.models import AirConditioners, AllAppliances
from tqdm import tqdm
import os
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
client = QdrantClient(
    url=os.getenv(
        "QDRANT_URL"
    ), 
    api_key=os.getenv(
        "QDRANT_API_KEY"
    ),
)
client.recreate_collection(
    collection_name="all_appliances",
    vectors_config=models.VectorParams(
        size=384,
        distance=models.Distance.COSINE
    )
)
ac = AllAppliances.objects.all()
model = SentenceTransformer('all-MiniLM-L6-v2')

for i in tqdm(ac,desc="Processing All Appliances"):
    vector = model.encode(
        i.name
    )
    client.upsert(
        collection_name="all_appliances",
        points=[
            models.PointStruct(
                id=i.id,
                vector=vector,
                payload={
                    "name": i.name,
                    "price": i.actual_price,
                    "image": i.image,
                    "main_category":i.main_category,
                    "sub_category":i.sub_category
                }
            )
        ]
    )
