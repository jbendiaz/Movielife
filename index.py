from flask import Flask, render_template

app = Flask(__name__)
"""
@app.route("/")
def principal():
	return "Bienvenido, pasen ahora"

@app.route("/contactos")
def contactos():
	return "Pagina de contactos"
"""

@app.route("/")
def principal():
	return  render_template("index.html")

@app.route("/registro")
def registro():
	return  render_template("Registro.html")

@app.route("/noticia")
def noticia():
	return  render_template("Noticia.html")

if __name__ == "__main__":
	app.run(debug=True, port=5022)