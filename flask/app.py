from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({ 
        "status": 200,
        "message": "Hello World"
    })

@app.route("/sala")
def sala():
    sala = ["Sala 1", "Sala 2", "Sala 3"]
    return jsonify({
        "status": 200,
        "sala": sala
    })

@app.route("/alunos", methods=["POST"])
def alunos():
    alunos = request.get_json()
    if alunos is None:
        return jsonify({
            "status": 400,
            "message": "Nenhum aluno foi enviado"
        }), 400
    return jsonify({
        "status": 200,
        "alunos": alunos
    })

if __name__ == "__main__":
    app.run(debug=True)

