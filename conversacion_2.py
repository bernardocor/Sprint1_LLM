
from openai import OpenAI
import PyPDF2

# Cliente API OpenAI (coloca aquí tu clave API)
client = OpenAI(api_key="removed")

def leer_pdf(ruta_pdf):
    """Lee y extrae texto completo de un archivo PDF."""
    texto = ""
    with open(ruta_pdf, "rb") as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina in lector.pages:
            texto += pagina.extract_text()
    return texto

def obtener_respuesta_gpt(prompt):
    """Envía un prompt a OpenAI y obtiene la respuesta generada."""
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en resumir cuentos en viñetas."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=500
    )
    return respuesta.choices[0].message.content

def guardar_conversacion(nombre_archivo, prompts, respuestas):
    """Guarda en un archivo .txt la conversación usuario-LLM."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for prompt, respuesta in zip(prompts, respuestas):
            archivo.write(f"Usuario: {prompt}\n")
            archivo.write(f"LLM: {respuesta}\n\n")

def main():
    """Función principal del script."""
    ruta_cuento = "cuento.pdf"
    archivo_conversacion = "conversacion_2.txt"

    cuento = leer_pdf(ruta_cuento)

    prompts = [
        "A partir del siguiente cuento, genera exactamente 5 viñetas que resalten sus elementos más importantes:\n\n" + cuento
    ]

    respuestas = [obtener_respuesta_gpt(prompts[0])]

    guardar_conversacion(archivo_conversacion, prompts, respuestas)

    # Mostrar resultado para confirmación
    print(respuestas[0])

if __name__ == "__main__":
    main()
