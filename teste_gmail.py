import imaplib
from config import EMAIL, SENHA_APP

try:
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(EMAIL, SENHA_APP)
    print("✅ Login realizado com sucesso!")
    imap.logout()

except Exception as erro:
    print("❌ Erro:", erro)