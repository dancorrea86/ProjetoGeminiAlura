from flask import Flask, render_template, request
import conexaoGemini

app = Flask(__name__)

pergunta = []
resposta = []

@app.route('/', methods=["GET","POST"])
def chat():
    if request.method == 'POST':
        pergunta.append(request.form.get("pergunta"))
        resposta.append(conexaoGemini.gerar_e_buscar_consulta(request.form.get("pergunta")))
        title = "Chat"
        return render_template("chat.html", title=title, len = len(pergunta), pergunta=pergunta, resposta=resposta)
    else:
        # pergunta.append("b")
        # resposta.append("b")
        title = "Chat"
        return render_template("chat.html", title=title, len = len(pergunta), pergunta=pergunta, resposta=resposta)


@app.route('/about')
def about():
    names = ["John", "Mary"]
    return render_template("about.html")


