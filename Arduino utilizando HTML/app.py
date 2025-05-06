from flask import Flask,request,render_template,redirect
import database
app = Flask(__name__)
app.secret_key = "lol"
ALUNO = "Rafael Italiano"
LED = 1 

@app.route("/")
def index():
    if request.method == "GET":
        iot = database.pegar_tabela()
        print(iot)
        return render_template("dispositivo.html",iot=iot)
    
@app.route("/alterar_dispositivo/<id>", methods = ["GET", "POST"])
def alterar(id):
    if request.method == "GET":
        return render_template("alterar.html",id=id)
    nome = request.form['nome']
    led = request.form['led']
    if led == "ligado":
        valor = 1
    else:
        valor = 2
        
    ip = request.form['ip']
    database.atualizar_valores(nome,valor,ip,id)
    return redirect("/")

if __name__== "__main__":
    app.run(debug=True)