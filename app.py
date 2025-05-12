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
        dispositivo = database.pegar_dispositivo(id)
        return render_template("alterar.html",id=id,dispositivo=dispositivo)
    nome = request.form["nome"]
    led = request.form.get("led",0) == "on"
    ip = request.form["ip"]
    rele = request.form.get("rele",0) == "on"
    lcd = request.form["lcd"]
    servo = request.form["servo"]

    database.atualizar_valores(id, nome, ip, led, rele, lcd, servo)
    return redirect("/")

if __name__== "__main__":
    app.run(debug=True)