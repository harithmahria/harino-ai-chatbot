import os

import httpx
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

for proxy_var in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"):
    os.environ.pop(proxy_var, None)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
openai_client = httpx.Client(timeout=30.0, trust_env=False)

SYSTEM_PROMPT = """You are Harino.ai Assistant, the website chatbot for Harino.ai.

Role:
- Help visitors understand Harino.ai, pricing, credits, AI models, use cases, and support/contact options.
- Answer in the same language as the user when possible. Default to Dutch.
- Be concise, clear, and helpful.

Rules:
- Use only the context provided below.
- Do not invent features, prices, guarantees, or policies.
- If the answer is not clearly in the context, say that you are not fully sure and refer the user to support@harino.ai.
- If the user asks about billing, custom deals, bugs, refunds, or account-specific issues, refer them to support@harino.ai.
- Keep answers short, usually 2 to 4 sentences.

Context:
{context}
"""

NO_CONTEXT_REPLY = (
    "Daar heb ik niet genoeg zekere informatie over. "
    "Neem voor de meest actuele details contact op via support@harino.ai."
)


def get_embedding(text):
    response = openai_client.post(
        "https://api.openai.com/v1/embeddings",
        json={"input": text, "model": "text-embedding-3-small"},
        headers={
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json",
        },
    )
    response.raise_for_status()
    return response.json()["data"][0]["embedding"]


def search_documents(query_embedding, match_count=6, threshold=0.18):
    result = supabase.rpc(
        "match_documents",
        {
            "query_embedding": query_embedding,
            "match_count": match_count,
            "match_threshold": threshold,
        },
    ).execute()
    return result.data or []


def build_context(docs):
    return "\n".join(f"- [{doc['category']}] {doc['content']}" for doc in docs)


def generate_answer(user_question, context_docs):
    if not context_docs:
        return NO_CONTEXT_REPLY

    response = openai_client.post(
        "https://api.openai.com/v1/chat/completions",
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT.format(context=build_context(context_docs)),
                },
                {"role": "user", "content": user_question},
            ],
            "temperature": 0.2,
            "max_tokens": 220,
        },
        headers={
            "Authorization": f"Bearer {OPENAI_KEY}",
            "Content-Type": "application/json",
        },
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def chat(user_question, session_id=None):
    embedding = get_embedding(user_question)

    docs = search_documents(embedding, match_count=6, threshold=0.18)
    if not docs:
        docs = search_documents(embedding, match_count=6, threshold=0.08)

    return generate_answer(user_question, docs)


if __name__ == "__main__":
    print("=" * 50)
    print("  Harino.ai Assistant")
    print("  Typ 'stop' om te stoppen")
    print("=" * 50)
    print()

    while True:
        question = input("Jij: ").strip()
        if not question:
            continue
        if question.lower() == "stop":
            print("Bot: Tot ziens.")
            break

        print(f"Bot: {chat(question)}")
        print()
