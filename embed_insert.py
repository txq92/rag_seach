import json
import chromadb
from chromadb.config import Settings
from nomic import embed

# Load checklist JSON
with open("checklist.json", "r", encoding="utf-8") as f:
    checklist = json.load(f)

# Khởi tạo Chroma client (giao tiếp với Docker qua HTTP)
client = chromadb.HttpClient(host="localhost", port=8001)

# Tạo collection nếu chưa có
collection = client.get_or_create_collection("checklist_rag")

# Tạo nội dung để embed (ghép title + description)
documents = []
ids = []
metadatas = []

for item in checklist:
    doc_text = f"{item['title']}. {item['description']}"
    documents.append(doc_text)
    ids.append(item["rule_id"])
    metadatas.append({
        "severity": item.get("severity", ""),
        "category": item.get("category", ""),
        "language": ", ".join(item.get("language", []))
    })

# Sử dụng nomic-embed-text
embedding_response = embed.text(texts=documents, model="nomic-embed-text-v1")
embeddings = embedding_response['embeddings']  # Lấy mảng embeddings từ response

# Insert vào Chroma
collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

print(f"✅ Đã insert {len(documents)} rule vào ChromaDB.")


print(f"✅ Test keets qua.")
# Embed câu truy vấn bằng model nomic-embed-text-v1
query = "console.log production"
query_embedding = embed.text(texts=[query], model="nomic-embed-text-v1")['embeddings']

# Query bằng embedding
results = collection.query(query_embeddings=query_embedding, n_results=1)
print(results)
# ...existing code...
