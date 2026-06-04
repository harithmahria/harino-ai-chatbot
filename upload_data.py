# ============================================
# Dit script doet 4 dingen:
# 1. Leest de Harino.ai data
# 2. Verwijdert oude data uit Supabase
# 3. Maakt embeddings via OpenAI API (in batches)
# 4. Upload alles naar Supabase
# ============================================

import os
import httpx
from dotenv import load_dotenv
from supabase import create_client
from data.harino_data import documents

# --- Stap 1: Environment variables laden ---
load_dotenv()
for proxy_var in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"):
    os.environ.pop(proxy_var, None)

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# --- Stap 2: Supabase client aanmaken ---
supabase = create_client(supabase_url, supabase_key)
openai_client = httpx.Client(timeout=120.0, trust_env=False)
print("Verbonden met Supabase!")


# --- Stap 3: Embedding functie ---
def get_embeddings(texts):
    """Maakt embeddings voor een lijst teksten via OpenAI."""
    response = openai_client.post(
        "https://api.openai.com/v1/embeddings",
        json={"input": texts, "model": "text-embedding-3-small"},
        headers={
            "Authorization": f"Bearer {openai_key}",
            "Content-Type": "application/json",
        },
    )
    response.raise_for_status()
    return [item["embedding"] for item in response.json()["data"]]


# --- Stap 4: Oude data verwijderen ---
print("\nOude documenten verwijderen...")
supabase.table("documents").delete().gte("id", 0).execute()
print("Klaar!")

# --- Stap 5: Embeddings maken in batches ---
print(f"\nEmbeddings maken voor {len(documents)} documenten...")

BATCH_SIZE = 50  # OpenAI kan ~2000 tegelijk, maar we doen 50 per batch
all_embeddings = []

for i in range(0, len(documents), BATCH_SIZE):
    batch = documents[i : i + BATCH_SIZE]
    texts = [doc["content"] for doc in batch]
    embeddings = get_embeddings(texts)
    all_embeddings.extend(embeddings)
    print(f"  Batch {i // BATCH_SIZE + 1}: {len(embeddings)} embeddings gemaakt")

print(f"Totaal: {len(all_embeddings)} embeddings ({len(all_embeddings[0])} dimensies)")

# --- Stap 6: Uploaden naar Supabase ---
print(f"\nUploaden naar Supabase...")

for i, doc in enumerate(documents):
    supabase.table("documents").insert({
        "content": doc["content"],
        "category": doc["category"],
        "embedding": all_embeddings[i],
    }).execute()

    if (i + 1) % 25 == 0 or i == len(documents) - 1:
        print(f"  [{i+1}/{len(documents)}] geupload...")

print(f"\nKlaar! {len(documents)} documenten geupload naar Supabase!")
print("Harino.ai chatbot is klaar!")
