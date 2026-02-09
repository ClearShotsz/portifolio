from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projetos")
def projetos():
    # Lista de projetos para exibir no template
    projetos = [
        {
            "nome": "Quiz de Informática Básica",
            "descricao": "Jogo educativo interativo para testar e reforçar conhecimentos em informática básica de forma simples e divertida.",
            "rota": "quiz"  # nome da rota para o botão
        },
        {
            "nome": "SENAC no Roblox – Recriação",
            "descricao": "Recriação do prédio do SENAC dentro do Roblox, focada em realismo, ambientes 3D e design de jogos.",
            "rota": "senac"
        }
    ]
    return render_template("projetos.html", projetos=projetos)

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/senac")
def senac():
    return render_template("senac.html")

@app.route("/redes")
def redes():
    return render_template("redes.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
