from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = ""
    estado = ""
    mostrar_resultado = False

    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            # Verificar que las notas y la asistencia estén dentro de los rangos
            if 10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70 and 0 <= asistencia <= 100:
                # Calcula promedio
                promedio = round((nota1 + nota2 + nota3) / 3, 1)

                # entrega valor (aprobado o reprobado)
                if promedio >= 40 and asistencia >= 75:
                    estado = "Aprobado"
                else:
                    estado = "Reprobado"

                mostrar_resultado = True
            else:
                estado = "Las notas deben estar entre 10 y 70, y la asistencia entre 0 y 100."

        except ValueError:
            estado = "Por favor, ingrese valores numéricos válidos."

    return render_template('ejercicio1.html', promedio=promedio, estado=estado,
                           mostrar_resultado=mostrar_resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mas_largo = ""
    longitud_mas_larga = ""
    mostrar_resultado = False

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Calcular largo de cada nombre
        longitud1 = len(nombre1)
        longitud2 = len(nombre2)
        longitud3 = len(nombre3)

        # Determinar nombre mas largo
        if longitud1 > longitud2 and longitud1 > longitud3:
            nombre_mas_largo = nombre1
            longitud_mas_larga = longitud1
        elif longitud2 > longitud1 and longitud2 > longitud3:
            nombre_mas_largo = nombre2
            longitud_mas_larga = longitud2
        elif longitud3 > longitud1 and longitud3 > longitud2:
            nombre_mas_largo = nombre3
            longitud_mas_larga = longitud3
        else:
            # si 2 o mas nombres son igual de largos
            nombre_mas_largo = "Hay nombres con la misma longitud máxima."
            longitud_mas_larga = longitud1  # Se elije el primer nombre mas largo
        mostrar_resultado = True

    return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo,
                           longitud_mas_larga=longitud_mas_larga, mostrar_resultado=mostrar_resultado)


if __name__ == '__main__':
    app.run(debug=True)
