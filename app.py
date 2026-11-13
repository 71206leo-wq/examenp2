from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/compra', methods=['GET', 'POST'])
def compra():
    resultado = None
    if request.method == 'POST':
        try:
            cantidad = float(request.form.get('cantidad', 0))
            precio = float(request.form.get('precio', 0))
            
            subtotal = cantidad * precio
            descuento = subtotal * 0.10 if subtotal > 1000 else 0.0
            total = subtotal - descuento
            
            resultado = {
                'cantidad': cantidad,
                'precio': precio,
                'subtotal': subtotal,
                'descuento': descuento,
                'total': total
            }
        except (ValueError, TypeError):
            resultado = {'error': 'Por favor ingresa valores numéricos válidos.'}
            
    return render_template('compra.html', resultado=resultado)

@app.route('/salario', methods=['GET', 'POST'])
def salario():
    resultado = None
    if request.method == 'POST':
        try:
            horas = float(request.form.get('horas', 0))
            pago_hora = float(request.form.get('pago_hora', 0))
            
            horas_normales = min(horas, 40)
            horas_extra = max(0, horas - 40)
            
            pago_normal = horas_normales * pago_hora
            pago_extra = horas_extra * (pago_hora * 2)
            salario_total = pago_normal + pago_extra
            
            resultado = {
                'horas': horas,
                'pago_hora': pago_hora,
                'horas_normales': horas_normales,
                'horas_extra': horas_extra,
                'pago_normal': pago_normal,
                'pago_extra': pago_extra,
                'salario_total': salario_total
            }
        except (ValueError, TypeError):
            resultado = {'error': 'Por favor ingresa valores numéricos válidos.'}
            
    return render_template('salario.html', resultado=resultado)

@app.route('/temperatura', methods=['GET', 'POST'])
def temperatura():
    resultado = None
    if request.method == 'POST':
        try:
            celsius = float(request.form.get('celsius', 0))
            fahrenheit = (celsius * 9 / 5) + 32
            kelvin = celsius + 273.15
            
            resultado = {
                'celsius': celsius,
                'fahrenheit': round(fahrenheit, 2),
                'kelvin': round(kelvin, 2)
            }
        except (ValueError, TypeError):
            resultado = {'error': 'Por favor ingresa un número válido para los grados Celsius.'}
            
    return render_template('temperatura.html', resultado=resultado)

@app.route('/empresa')
def empresa():
    return render_template('empresa.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if _name_ == '_main_':
    app.run(debug=True)