# RH Inteligente com Gemini

Projeto da disciplina de Inteligência Artificial / Automação de Processos.

## Funcionalidades

- Recebe currículos por e-mail (Gmail).
- Lê PDFs automaticamente.
- Analisa o currículo usando IA Gemini.
- Salva os candidatos em SQLite.
- Envia resposta automática ao candidato.

## Tecnologias

- Python 3.13
- Google Gemini API
- SQLite
- PyMuPDF
- IMAP/SMTP (Gmail)

## Instalação

```bash
pip install -r requirements.txt
```

Edite o arquivo `config.py` com sua chave do Gemini e a senha de aplicativo do Gmail.

Execute:

```bash
py main.py
```