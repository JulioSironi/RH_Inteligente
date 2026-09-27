from google import genai
import json
from config import GEMINI_API_KEY

# Inicializa o cliente Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

def analisar_curriculo(texto):
    prompt = f"""
Você é um analista de RH.

Analise o currículo abaixo e retorne APENAS um JSON válido.

Formato:

{{
  "nome": "",
  "email": "",
  "telefone": "",
  "vaga": "",
  "nivel": "",
  "habilidades": [],
  "resumo": ""
}}

Currículo:
{texto}
"""

    resposta = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    texto_json = resposta.text.strip()

    # Remove blocos Markdown caso o Gemini responda assim
    texto_json = texto_json.replace("```json", "").replace("```", "").strip()

    return json.loads(texto_json)