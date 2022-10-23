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

@app.route("/warner")
def warner():
	return  render_template("Warner.html")

@app.route("/marvel")
def marvel():
	return  render_template("Marvel.html")

@app.route("/dc")
def dc():
	return  render_template("DC Comic.html")

@app.route("/disney")
def disney():
	return  render_template("Disney.html")

@app.route("/estrenos")
def estrenos():
	return  render_template("Estrenos.html")

@app.route("/eventos")
def eventos():
	return  render_template("Eventos.html")

@app.route("/warnere")
def warnere():
	return  render_template("WarnerE.html")

@app.route("/marvele")
def marvele():
	return  render_template("MarvelE.html")

@app.route("/disneye")
def disneye():
	return  render_template("DisneyE.html")

@app.route("/dce")
def dce():
	return  render_template("DC ComicE.html")

@app.route("/todas_las_peliculas")
def tpeliculas():
	return  render_template("Todas las pelis.html")

@app.route("/peliculas_recientes")
def rpeliculas():
	return  render_template("Recientes.html")

if __name__ == "__main__":
	app.run(debug=True, port=5022)