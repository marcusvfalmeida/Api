from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

def conectar_banco():
    STRING_BANCO = os.getenv('NEON_DB')
    return psycopg.connect(STRING_BANCO)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message':'API RODANDO'})

@app.route('/jogos', methods=['GET'])
def consultar_jogos():
    with conectar_banco().cursor() as cursor:
        cursor.execute('SELECT * FROM jogos')
        resposta = cursor.fetchall()
    return jsonify(resposta)

@app.route('/jogos/<int:jogo_id>', methods=['GET'])
def consultar_jogo(jogo_id):
    with conectar_banco().cursor() as cursor:
        cursor.execute('SELECT * FROM jogos WHERE id=%s',
                       (jogo_id,)
                       )
        resposta = cursor.fetchall()
        if resposta == []:
            resposta = {'message':'No data found'}
    return jsonify(resposta)

@app.route('/cadastrar',methods=['POST'])
def cadastrar_jogo():
    try:
        dados = request.get_json()
        nome = dados.get('nome')
        ano = dados.get('ano')
        if not nome or ano is None:
            return jsonify({'message':'Informe nome e ano'})
        with conectar_banco() as conn:
            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO jogos (nome, ano) VALUES (%s,%s) RETURNING id, nome, ano;',
                            (nome,ano)
                            )
                jogo = cursor.fetchone()
            conn.commit()
        return jsonify(jogo)
    except Exception:
        app.logger.exception('Erro ao cadastrar produto')
        return jsonify({'erro':'Não foi possível cadastrar'}),500

@app.route('/editar',methods=['PUT'])
def editar_jogo():
    try:
        dados = request.get_json()
        nome = dados.get('nome')
        ano = dados.get('ano')
        id_jogo = dados.get('id')
        if not nome or ano is None or id_jogo is None:
            return jsonify({'message':'Informe id, nome, ano'})
        with conectar_banco() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                               UPDATE jogos 
                               SET nome = %s,
                               ano = %s
                               WHERE id = %s 
                               RETURNING id, nome, ano''',
                                (nome,ano,id_jogo)
                                )
                jogo = cursor.fetchone()
            conn.commit()
        return jsonify(jogo)
    except Exception:
        app.logger.exception('Erro ao cadastrar produto')
        return jsonify({'erro':'Não foi possível alterar'}),500


app.run(debug=True)