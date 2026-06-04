# Harino.ai Chatbot

RAG chatbot for Harino.ai built with Flask, Supabase pgvector, and OpenAI.

## Tech Stack

- Python Flask backend
- HTML/CSS/JavaScript frontend
- Supabase PostgreSQL database
- pgvector for semantic search
- OpenAI embeddings and chat completions

## How It Works

1. Knowledge content is stored in `data/harino_data.py`.
2. `upload_data.py` creates OpenAI embeddings for each document.
3. The documents are uploaded to Supabase in the `documents` table.
4. When a user asks a question, `rag.py` embeds the question and searches Supabase for relevant context.
5. OpenAI generates an answer using the retrieved Harino.ai context.

## Local Setup

Create a `.env` file with:

```text
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_secret_key
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## Deployment

Production start command:

```bash
gunicorn app:app
```
