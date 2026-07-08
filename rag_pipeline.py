import chromadb

# 1. Client = your connection to the vector store (like the client in your API script)
client = chromadb.Client()

# 2. Collection = a container holding your chunks + their embeddings
collection = client.get_or_create_collection(name="animal_facts")

# 3. Your 10 text chunks (the "documents" to search through)
chunks = [
    "Dogs are loyal animals that bark and love to play fetch.",
    "Cats are independent pets that purr and sleep a lot.",
    "Elephants are the largest land animals and have long trunks.",
    "Penguins are birds that cannot fly but are excellent swimmers.",
    "Lions are big cats that live in groups called prides.",
    "Dolphins are highly intelligent marine mammals.",
    "Owls are nocturnal birds with excellent night vision.",
    "Kangaroos are marsupials that carry their young in pouches.",
    "Bees produce honey and are vital for pollinating plants.",
    "Sharks are fish with powerful jaws and rows of sharp teeth.",
]

# 4. Add chunks to the collection. Chroma automatically embeds them.
#    Each needs a unique id, so we generate id0, id1, id2...
collection.add(
    documents=chunks,
    ids=[f"id{i}" for i in range(len(chunks))],
)

# 5. Ask a question and retrieve the top 2 most relevant chunks
query = "who is the goat of basketball"
results = collection.query(
    query_texts=[query],
    n_results=2,
)

# 6. Print the results
print(f"Query: {query}\n")
print("Top 2 relevant chunks:")
for doc in results["documents"][0]:
    print(f"- {doc}")

import anthropic

# Combine the retrieved chunks into one context string
retrieved_chunks = results["documents"][0]
context = "\n".join(retrieved_chunks)

# Build a prompt that gives Claude the context and the question
prompt = f"""Use the following context to answer the question.

Context:
{context}

Question: {query}

Answer based only on the context above."""

# Send it to Claude
anthropic_client = anthropic.Anthropic()
response = anthropic_client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    messages=[
        {"role": "user", "content": prompt}
    ],
)

# Print Claude's answer
print("\nClaude's answer using the retrieved context:")
print(response.content[0].text)