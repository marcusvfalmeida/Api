from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/')
def inicio():
    return jsonify({'message':'API rodando'})

@app.get('/teste')
def teste():
    return jsonify({'mensagem':'testando'})

@app.get('/cavaleiro/<mes>')
def signo(mes):
    cavaleiros_de_ouro = {
    "Janeiro": {"signo": "Aquário", "cavaleiro": "Camus"},
    "Fevereiro": {"signo": "Peixes", "cavaleiro": "Afrodite"},
    "Março": {"signo": "Áries", "cavaleiro": "Mu"},
    "Abril": {"signo": "Touro", "cavaleiro": "Aldebaran"},
    "Maio": {"signo": "Gêmeos", "cavaleiro": "Saga"},
    "Junho": {"signo": "Câncer", "cavaleiro": "Máscara da Morte"},
    "Julho": {"signo": "Leão", "cavaleiro": "Aiolia"},
    "Agosto": {"signo": "Virgem", "cavaleiro": "Shaka"},
    "Setembro": {"signo": "Libra", "cavaleiro": "Dohko"},
    "Outubro": {"signo": "Escorpião", "cavaleiro": "Milo"},
    "Novembro": {"signo": "Sagitário", "cavaleiro": "Aiolos"},
    "Dezembro": {"signo": "Capricórnio", "cavaleiro": "Shura"}
}
    return jsonify(cavaleiros_de_ouro[mes.capitalize()])

app.run(debug=True)