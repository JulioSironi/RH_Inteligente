import sqlite3

con = sqlite3.connect("database/candidatos.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM candidatos")
dados = cursor.fetchall()

print("=" * 70)
print("CANDIDATOS CADASTRADOS")
print("=" * 70)

for candidato in dados:
    print(f"ID: {candidato[0]}")
    print(f"Nome: {candidato[1]}")
    print(f"E-mail: {candidato[2]}")
    print(f"Telefone: {candidato[3]}")
    print(f"Vaga: {candidato[4]}")
    print(f"Nível: {candidato[5]}")
    print(f"Habilidades: {candidato[6]}")
    print(f"Resumo: {candidato[7]}")
    print("-" * 70)

con.close()