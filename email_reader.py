import imaplib
import email
from pathlib import Path
from config import EMAIL, SENHA_APP

Path("curriculos").mkdir(exist_ok=True)


def buscar_curriculos():

    arquivos = []

    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(EMAIL, SENHA_APP)
    imap.select("INBOX")

    status, mensagens = imap.search(None, "UNSEEN")

    for numero in mensagens[0].split():

        _, dados = imap.fetch(numero, "(RFC822)")
        mensagem = email.message_from_bytes(dados[0][1])

        remetente = mensagem["From"]

        for parte in mensagem.walk():

            if parte.get_content_disposition() == "attachment":

                nome = parte.get_filename()

                caminho = Path("curriculos") / nome

                with open(caminho, "wb") as arquivo:
                    arquivo.write(parte.get_payload(decode=True))

                arquivos.append({
                    "email": remetente,
                    "arquivo": str(caminho)
                })

    imap.logout()

    return arquivos