import sqlite3
from pathlib import Path

Path("database").mkdir(exist_ok=True)

con = sqlite3.connect("database/candidatos.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidatos(

id INTEGER PRIMARY KEY AUTOINCREMENT,

nome TEXT,
email TEXT,
telefone TEXT,
vaga TEXT,
nivel TEXT,
habilidades TEXT,
resumo TEXT

)
""")

con.commit()


def salvar_candidato(candidato):

    cursor.execute("""
INSERT INTO candidatos
(nome,email,telefone,vaga,nivel,habilidades,resumo)

VALUES(?,?,?,?,?,?,?)

""", (

        candidato["nome"],
        candidato["email"],
        candidato["telefone"],
        candidato["vaga"],
        candidato["nivel"],
        ", ".join(candidato["habilidades"]),
        candidato["resumo"]

    ))

    con.commit()


def listar_candidatos():

    cursor.execute("SELECT * FROM candidatos")

    return cursor.fetchall()