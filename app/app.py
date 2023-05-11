from flask import Flask, render_template, request
from datetime import datetime, date

app = Flask(__name__)

@app.route("/")
def index():
    print("Funcion Index")
    datos = {'titulo': 'Index', 'bienvenida': "Hola desde Flask con html y datos!"}
    return render_template('index.html', data=datos)

@app.route("/cursos")
def cursos():
    print("Funcion Cursos")
    cursos = ["Python","Backend","Frontend","Datos","Sistemas Operativos"]
    datos = {'titulo':'Cursos', 'presentacion':"Estos son los cursos", 'cursos':cursos}
    return render_template('cursos.html', data=datos)

@app.route("/saludar/<nombre>")
def saludar(nombre):
    print("Funcion saludar", nombre)
    datos = {'titulo':'Saludar','nombre':nombre}
    return render_template('saludar.html',data=datos)

@app.route("/cumple")
def cumple():
    print("Funcion cumple")
    #print(request)
    #print(request.args)
    
    # Obtengo el nombre del parametro nombre del HTTPP GET (http://127.0.0.1:5000/cumple?nombre=ailen&fecnac=0211)
    nombre = request.args.get("nombre")
    
    # Obtengo la fecha de nacimiento del parametro fecnac del HTTPP GET (http://127.0.0.1:5000/cumple?nombre=ailen&fecnac=0211)
    fecha_nacimiento = request.args.get("fecnac")
    #print("fecha_nacimiento:", fecha_nacimiento)
    
    # Obtengo la fecha de hoy de la libreria date del modulo datetime
    fecha_hoy = date.today()
    #print("fecha_hoy:", fecha_hoy)
    
    # Convierto la fecha de hoy en un string con el formato que quiero (dia y mes ddmm) 
    fecha_str = fecha_hoy.strftime('%d%m')
    #print("fecha_str:", fecha_str)
            
    if fecha_nacimiento == fecha_str:
        mensaje = "Feliz cumple! "
        es_cumple = True
    else:
        mensaje = "Feliz NO cumple! "
        es_cumple = False
    
    datos = {'titulo':'Cumple', "nombre": nombre, "mensaje": mensaje, "cumple": es_cumple}
    return render_template('cumple.html',data=datos)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
