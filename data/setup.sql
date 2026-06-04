-- ============================================
-- Harino.ai Chatbot - Supabase Setup
--
-- Draai dit script EEN KEER in de Supabase SQL editor.
-- Het maakt een schone setup met de juiste vector dimensie (1536)
-- voor het OpenAI model text-embedding-3-small.
-- ============================================

-- STAP 1: pgvector extensie aanzetten
create extension if not exists vector;

-- STAP 2: Oude tabellen / functies opruimen (van eerdere setups)
drop function if exists match_documents(vector, int, float);
drop function if exists match_documents(vector(384), int, float);
drop function if exists match_documents(vector(1024), int, float);
drop function if exists match_documents(vector(1536), int, float);
drop table if exists documents;
drop table if exists reservations;

-- STAP 3: Documents tabel (1536 dimensies = text-embedding-3-small)
create table documents (
  id bigserial primary key,
  content text not null,
  category text not null,
  embedding vector(1536)
);

-- STAP 4: Index voor snelle vector search
create index on documents
  using ivfflat (embedding vector_cosine_ops)
  with (lists = 10);

-- STAP 5: Zoekfunctie (cosine similarity)
create or replace function match_documents (
  query_embedding vector(1536),
  match_count int default 5,
  match_threshold float default 0.15
)
returns table (
  id bigint,
  content text,
  category text,
  similarity float
)
language plpgsql
as $$
begin
  return query
  select
    documents.id,
    documents.content,
    documents.category,
    1 - (documents.embedding <=> query_embedding) as similarity
  from documents
  where 1 - (documents.embedding <=> query_embedding) > match_threshold
  order by documents.embedding <=> query_embedding
  limit match_count;
end;
$$;
