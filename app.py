import pyodbc
from flask import Flask, render_template, request, redirect

from models.persona import Persona
from controllers.listar_controller import listarpersonas, listarclientes
from controllers.persona_controller import insertar_persona

app = Flask(__name__)


@app.route("/")
def inicio():
    personas = listarpersonas()
    return render_template("index.html", personas=personas)


@app.route("/clientes")
def clientes():
    clientes_lista = listarclientes()
    return render_template("clientes.html", clientes=clientes_lista)


@app.route("/nuevo")
def nuevo():
    return render_template("insertar.html")


@app.route("/guardar", methods=["POST"])
def guardar():
    persona = Persona(
        request.form.get("tipo_persona"),
        request.form.get("nombres"),
        request.form.get("apaterno"),
        request.form.get("amaterno"),
        request.form.get("razon_social"),
        request.form.get("nombre_comercial"),
        int(request.form.get("id_tipo_documento")),
        request.form.get("numero_documento"),
        request.form.get("telefono"),
        request.form.get("email"),
        int(request.form.get("id_nacionalidad")),
        request.form.get("estado"),
    )

    try:
        insertar_persona(persona)
    except pyodbc.IntegrityError as error:
        if "uq_persona_documento" in str(error):
            mensaje = "No se pudo registrar: el tipo y número de documento ya existen."
        else:
            mensaje = "No se pudo registrar: verifica los datos relacionados."

        return render_template("insertar.html", error=mensaje), 400

    return redirect("/")

    insertar_persona(persona)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)