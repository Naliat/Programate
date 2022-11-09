import sqlite3

empregados = [
                {'nome':'jadson', 'cargo':'analista', 'salario': 5000},
                {'nome':'tailan', 'cargo':'analista', 'salario': 5000},
                {'nome':'edival', 'cargo':'desenvolvedor', 'salario': 6000}
             ]

conn = sqlite3.connect('interprise.db')

cursor = conn.cursor()

for empregado in empregados:
    cursor.execute("""
                INSERT INTO empregados (nome, cargo, salario)
                VALUES (?, ?, ?)
        """, (empregado['nome'], empregado['cargo'], empregado['salario']))

print("Dados inseridos com sucesso")

conn.commit()
conn.close()