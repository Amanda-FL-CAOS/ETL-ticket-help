from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_ticket(text):

    prompt = f"""
    Analise o chamado abaixo.

    Retorne APENAS:
    - Categoria
    - Prioridade
    - Sentimento

    Chamado:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content