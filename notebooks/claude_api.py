import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    system="You are a helpful assistant that explains things clearly and concisely.",
    messages=[
        {"role": "user", "content": "Explain what an API is in two sentences."}
    ],
)

print("Claude's response:")
print(message.content[0].text)

print("\nToken usage:")
print(f"Input tokens: {message.usage.input_tokens}")
print(f"Output tokens: {message.usage.output_tokens}")