from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

texto = input("Escribe tu idea o texto: ")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Eres un asistente de escritura profesional."},
        {"role": "user", "content": f"Mejora este texto y hazlo más claro y formal:\n\n{texto}"}
    ]
)

print("\nResultado:\n")
print(response.choices[0].message.content)
