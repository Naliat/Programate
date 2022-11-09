import sqlite3

#empregados = [
#                {'nome':'jadson', 'cargo':'analista', 'salario': 5000},
#                {'nome':'tailan', 'cargo':'analista', 'salario': 5000},
#                {'nome':'edival', 'cargo':'desenvolvedor', 'salario': 6000}
#             ]

conn = sqlite3.connect('interprise.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE empregados (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT,
        salario REAL
    );
""")

print("tabela criada com sucesso!")

conn.close()