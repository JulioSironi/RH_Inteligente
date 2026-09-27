from email_reader import buscar_curriculos
from pdf_reader import extrair_texto_pdf
from gemini_ai import analisar_curriculo
from database import salvar_candidato
from email_sender import enviar_confirmacao

print("=" * 50)
print("      RH INTELIGENTE COM GEMINI")
print("=" * 50)

curriculos = buscar_curriculos()

if len(curriculos) == 0:
    print("Nenhum currículo novo encontrado.")
    exit()

for item in curriculos:

    print(f"\nCurrículo encontrado: {item['arquivo']}")

    texto = extrair_texto_pdf(item["arquivo"])

    print("Analisando com IA Gemini...")

    candidato = analisar_curriculo(texto)

    salvar_candidato(candidato)

    enviar_confirmacao(item["email"], candidato["nome"])

    print("\nANÁLISE FINAL")
    print("-" * 40)

    print("Nome:", candidato["nome"])
    print("Email:", candidato["email"])
    print("Telefone:", candidato["telefone"])
    print("Vaga:", candidato["vaga"])
    print("Nível:", candidato["nivel"])
    print("Habilidades:", ", ".join(candidato["habilidades"]))
    print("Resumo:", candidato["resumo"])

    print("-" * 40)
    print("Salvo no banco SQLite.")
    print("Resposta enviada ao candidato.")

print("\nProcesso concluído.")