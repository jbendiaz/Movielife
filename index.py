from flask import Flask, render_template, request, url_for, redirect, jsonify, flash 
from flask_mysqldb import MySQL
from config import config 
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User 

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@app.before_request
def before_request():
	print("Antes de...")

@app.after_request
def after_request(response):
	print("Despues de...")
	return response

@app.route("/login/inicio")
def indexlogin():
	return  render_template("/login/index.html")

@app.route("/login/noticia")
def noticialogin():
	return  render_template("/login/Noticia.html")

@app.route("/login/warner")
def warnerlogin():
	return  render_template("/login/Warner.html")

@app.route("/login/marvel")
def marvelogin():
	return  render_template("/login/Marvel.html")

@app.route("/login/dc")
def dclogin():
	return  render_template("/login/DC Comic.html")

@app.route("/login/disney")
def disneylogin():
	return  render_template("/login/Disney.html")

@app.route("/login/estrenos")
def estrenoslogin():
	return  render_template("/login/Estrenos.html")

@app.route("/login/eventos")
def eventoslogin():
	return  render_template("/login/Eventos.html")

@app.route("/login/warnere")
def warnerelogin():
	return  render_template("/login/WarnerE.html")

@app.route("/login/marvele")
def marvelelogin():
	return  render_template("/login/MarvelE.html")

@app.route("/login/disneye")
def disneyelogin():
	return  render_template("/login/DisneyE.html")

@app.route("/login/dce")
def dcelogin():
	return  render_template("/login/DC ComicE.html")

@app.route("/login/todas_las_peliculas")
def tpeliculaslogin():
	return  render_template("/login/Todas las pelis.html")

@app.route("/login/peliculas_recientes")
def rpeliculaslogin():
	return  render_template("/login/Recientes.html")




@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")

@app.route("/inicio_de_sesion", methods=["GET", "POST"])
def principal():
	if request.method == "POST":
		user = User(0, request.form["username"], request.form["password"])
		logged_user = ModelUser.principal(db, user)
		if logged_user != None:
			if logged_user.password:
				login_user(logged_user)
				return redirect(url_for('indexlogin'))
			else:
				flash("CLave Incorrecta")
				return render_template("login.html")
		else:
			flash("Error de Usuario")
			return render_template("login.html")
	else:
		return  render_template("login.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

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




def query_string():
	print(request)
	print(request.args)
	print(request.args.get("param1"))
	return "ok"

#@app.route("/usuario")
#def list_usuario():
#	data={}
#	try:
#		cursor = conexion.connection.cursor()
#		slq = "SELECT * FROM `usuario` WHERE 1"
#		cursor.execute(sql)
#		usuario = cursor.fetchall()
#		data["mensaje"] = "Excelente..."
#	except Exception as ex:
#		data["mensaje"] = "Error..."
#	return jsonify(data)

def status_404(error):
	#return render_template("404.html"), 404
	return redirect(url_for("index"))

#def status_405(error):
    #return redirect(url_for('principal'))

if __name__ == "__main__":
	app.config.from_object(config['development'])
	app.add_url_rule("/query_string", view_func=query_string)
	#app.register_error_handler(405, status_405)
	app.register_error_handler(404, status_404)
	app.run(port=5022)