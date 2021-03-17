from flask import Flask, render_template, request
from datetime import date
from datetime import datetime

def fechaHoy():
  return date.today()

def cargarNotas():
  pass

class Nota:
  def __init__(self, fecha, titulo, descripcion):
    self.fecha = fecha
    self.titulo = titulo
    self.descripcion = descripcion

def guardarNota(fecha, titulo, descripcion):
  nuevanota = Nota(fecha, titulo, descripcion)
  notas.append(nuevanota)


app = Flask(__name__)
notas = []


@app.route('/')
def main():
  if request.method == "GET":
    titulo = request.args.get("titulo")
    descripcion = request.args.get("descripcion")
    if(titulo!=None or descripcion!=None):
      guardarNota(fechaHoy(), titulo, descripcion)    
  return render_template('index.html', notas = notas, fechaHoy = fechaHoy())

  
if __name__ == '__main__':
  app.run(debug=True)


