from flask import Flask, make_response, request

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

import datetime
import StringIO
import math

app = Flask(__name__)

def f(x, a, b):
    return a * math.sin(b * x)

@app.route("/grafica")
def simple():
    # Recuperamos el parametro a y b
    a = float(request.args.get("a", "1"))
    b = float(request.args.get("b", "1"))

    # Creamos una figura (una grafica)
    fig = Figure()
    # Creamos un eje (una grafica 1 row 1 col)
    ax = fig.add_subplot(111)

    # Definimos los puntos
    X = []
    Y = []

    for t in range(-100, 100):
        x = t / 80.
        y = f(x, a, b)
        X.append(x)
        Y.append(y)

    # Graficamos los puntos en rojo
    ax.plot(X, Y, "r-")

    # Transformamos la figura (la grafica) en un canvas
    canvas = FigureCanvas(fig)

    # Creamos un flujo de texto para grabar nuestro canvas
    png_output = StringIO.StringIO()

    # Imprimo el canvas en flujo de texto
    canvas.print_png(png_output)

    # Creo una respuesta con mi texto
    response = make_response(png_output.getvalue())
    
    # Le digo a la respuesta que el contenido es una imagen png
    response.headers['Content-Type'] = 'image/png'

    # Envio la respuesta
    return response

app.run()