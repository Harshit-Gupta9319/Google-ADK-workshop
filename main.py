from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Hello! Explain AI in one sentence."
)

print(response.text)