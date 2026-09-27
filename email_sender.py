# Gmail SMTP sender placeholder
import smtplib
from email.message import EmailMessage
from config import EMAIL, SENHA_APP


def enviar_confirmacao(destino, nome):

    mensagem = EmailMessage()

    mensagem["Subject"] = "Currículo recebido com sucesso"
    mensagem["From"] = EMAIL
    mensagem["To"] = destino

    mensagem.set_content(f"""
Olá {nome},

Recebemos seu currículo com sucesso.

Ele foi analisado automaticamente pelo sistema RH Inteligente.

Obrigado pelo interesse na vaga.

Equipe RH
""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(EMAIL, SENHA_APP)

        smtp.send_message(mensagem)