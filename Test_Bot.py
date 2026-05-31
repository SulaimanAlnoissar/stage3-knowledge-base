from google import genai

client = genai.Client()

files = [
    "club_info.md",
    "committees.md",
    "activities.md",
    "knowledge_snippets.md",
    "faq.md"
]

knowledge_base = ""

for file_name in files:
    with open(file_name, "r", encoding="utf-8") as file:
        knowledge_base += f"\n\n--- {file_name} ---\n"
        knowledge_base += file.read()

question = input("Ask the bot: ")

prompt = f"""
You are a chatbot for GDG KSU.

Answer the user's question using only the information from the Knowledge Base below.
If the answer is not available in the Knowledge Base, say that the information is not available.

Knowledge Base:
{knowledge_base}

User Question:
{question}

Answer clearly and simply.
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print("\nBot Answer:")
print(response.text)