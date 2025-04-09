
from openai import OpenAI

# Configura tu clave API aquí
client = OpenAI(api_key="removed")

# Lee el archivo con el texto
with open("news_digital_bank.txt", "r", encoding="utf-8") as archivo:
    contenido_texto = archivo.read()

# Construye el prompt
prompt_resumen = (
    f"Resume el siguiente texto en español, en exactamente dos párrafos:\n\n{contenido_texto}\n\n"
)

# Llamada a la API actualizada para OpenAI>=1.0.0
respuesta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente que genera resúmenes precisos y concisos."},
        {"role": "user", "content": prompt_resumen},
    ],
    temperature=0.3,
    max_tokens=500
)

# Obtener la respuesta generada
resumen = respuesta.choices[0].message.content

# Añadir el tercer párrafo con información del diario y título
tercer_parrafo = (
    "\n\n"
    "Este resumen se generó a partir de una noticia titulada "
    "'Banca requiere elevar nivel de digitalización sin disminuir seguridad', "
    "publicada en el diario El Financiero."
)

# Muestra el resultado final
print(resumen + tercer_parrafo)
