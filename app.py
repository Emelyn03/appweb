from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resolver', methods=['POST'])
def resolver():
    try:
        a1 = float(request.form['a1'])
        b1 = float(request.form['b1'])
        c1 = float(request.form['c1'])
        a2 = float(request.form['a2'])
        b2 = float(request.form['b2'])
        c2 = float(request.form['c2'])

        coef_2v = [[a1, b1], [a2, b2]]
        const_2v = [c1, c2]

        solucion = np.linalg.solve(coef_2v, const_2v)
        solucion_texto = f"x = {solucion[0]:.2f}, y = {solucion[1]:.2f}"
    except np.linalg.LinAlgError:
        solucion_texto = "Sistema sin solución o con infinitas soluciones"
    except Exception as e:
        solucion_texto = f"Error en los datos: {e}"

    return render_template('index.html', solucion=solucion_texto)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
