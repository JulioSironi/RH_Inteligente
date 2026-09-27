import pymupdf as fitz

def extrair_texto_pdf(caminho_pdf):

    texto = ""

    documento = fitz.open(caminho_pdf)

    for pagina in documento:
        texto += pagina.get_text()

    documento.close()

    return texto