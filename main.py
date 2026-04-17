from openai import OpenAI

# Crear cliente (usa tu API key desde variable de entorno)
client = OpenAI()

# Pedir input al usuario
texto = input("Escribe tu idea o texto: ")

# Generar respuesta
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Eres un asistente de escritura profesional."},
        {"role": "user", "content": f"Mejora este texto y hazlo más claro y formal:\n\n{texto}"}
    ]
)

# Mostrar resultado
print("\nResultado:\n")
print(response.choices[0].message.content)