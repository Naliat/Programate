from flask import Flask, request, Response, g
import sqlite3


app = Flask(__name__)
DB_URL = "interprise.db"
#empregados = [
#               {'nome':'jadson', 'cargo':'analista', 'salario': 5000},
#                {'nome':'tailan', 'cargo':'analista', 'salario': 5000},
#                {'nome':'edival', 'cargo':'desenvolvedor', 'salario': 6000}
#             ]

users = [
            {"username":"jadson", "secret":"@admin456"}
        ]

@app.before_request
def before_request():
    print("Conectando ao banco")
    conn = sqlite3.connect(DB_URL)
    g.conn = conn

@app.teardown_request
def after_request(exception):
    if g.conn is not None:
        g.conn.close()
        print("Desconectando ao banco")

def query_empoyers_to_dict(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)

    employers_dict = [{'nome':row[0], 'cargo':row[1], 'salario':row[2]}
        for row in cursor.fetchall()]

    return employers_dict

def check_user(username, secret):
    for user in users:
        if(user["username"] == username) and (user["secret"] ==secret):
            return True
    return False


@app.route("/")
def home():
    return "<h1> Home Page</h1>"

@app.route("/empregados")
def get_empregados():
    
    query = """
        SELECT nome, cargo, salario
        FROM empregados;
    """

    employers_dict = query_empoyers_to_dict(g.conn, query)

    return {'empregados': employers_dict}

@app.route("/empregados/<cargo>")
def get_empregados_cargo(cargo):
    
    query = """
        SELECT nome, cargo, salario
        FROM empregados
        WHERE "cargo" LIKE "{}";
    """.format(cargo)

    employers_dict = query_empoyers_to_dict(g.conn, query)

    return {'empregados': employers_dict}

@app.route("/empregados/<info>/<value>")
def get_empregados_info(info, value):

    if value.isnumeric():
        value = float(value)

    query = """
        SELECT nome, cargo, salario
        FROM empregados
        WHERE "{}" LIKE "{}";
    """.format(info, value)

    employers_dict = query_empoyers_to_dict(g.conn, query)

    return {'empregados': employers_dict}


@app.route("/informations", methods = ['POST'])
def get_empregados_post():

    username = request.form['username']
    secret = request.form['secret']

    if not check_user(username, secret):
        return Response("UNAUTHORIZED", status=401)

    info = request.form['info']
    value = request.form['value']

    if value.isnumeric():
        value = float(value)

    query = """
        SELECT nome, cargo, salario
        FROM empregados
        WHERE "{}" LIKE "{}";
    """.format(info, value)

    employers_dict = query_empoyers_to_dict(g.conn, query)
    
    return {'empregados': employers_dict}

@app.route("/register", methods = ['POST'])
def add_empregados_post():

    username = request.form['username']
    secret = request.form['secret']

    if not check_user(username, secret):
        return Response("UNAUTHORIZED", status=401)
    nome = request.form['nome']
    cargo = request.form['cargo']
    salario = request.form['salario']

    query = """
        INSERT INTO empregados (nome, cargo, salario)
        VALUES ("{}", "{}", "{}");
    """.format(nome, cargo, salario)

    cursor = g.conn.cursor()
    cursor.execute(query)

    g.conn.commit()
    
    return {'empregados': "Registered employer"}

if __name__ == "__main__":
    app.run(debug=True)