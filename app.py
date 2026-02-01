from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    datos = {
        "titulo": "ANÁLISIS DE SISTEMAS",
        "nombre": "Edras Fernando.",
        "curso": "Ingeniería en Sistemas",
        "docente": "Ing. Juan Pérez",
        "institucion": "Universidad",
        "fecha": "15 de enero de 2026"
    }
    return render_template("caratula.html", **datos)

if __name__ == "__main__":
    app.run(debug=True)
