from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Length


app = Flask(__name__)
app.config['SECRET_KEY'] = 'llavesecreta'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LflO5oUAAAAAKgn-5g34tIXP6A-u7Lwy329viwp'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LflO5oUAAAAAEjJwu713AleKyV1vGPScywY9keu'

# MIENTRAS SE ESTÁ TESTEANDO = False para activar el reCAPTCHA y True para desactivarlo
app.config['TESTING'] = False
 
# Formulario
class PedidoForm(FlaskForm):
    nombre = TextField('Nombre', validators = [InputRequired(), Length(min=5, max=-1, message='El nombre debe tener al menos 5 caracteres.')])
    telefono = IntegerField('Teléfono', validators = [InputRequired()])
    direccion = TextAreaField('Dirección', validators = [InputRequired()])
    comentarios = TextAreaField('Comentarios')
    recaptcha = RecaptchaField()
   
# RUTAS
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
    form = PedidoForm()

    if form.validate_on_submit():
        return '<h1>Su pedido ha sido enviado satisfactoriamente con los siguientes datos de envío: <div> Nombre: {}<div> Teléfono: {}<div> Dirección: {}<div> Comentarios: {}'.format(form.nombre.data, form.telefono.data, form.direccion.data, form.comentarios.data)
    return render_template('form.html', form = form)

    l=[]
    producto1 ={ "Gaseosa 1.5L": 2500}
    producto2 ={ "Gaseosa 3L": 5000}
    producto3 ={ "Caramelo": 200}
    producto4 ={ "Leche": 2500}
    producto5 ={ "Papitas de pollo": 1600}
    producto6 ={ "DeTodito": 2000}
    producto7 ={ "Empanadas": 2000}
    producto8 ={"Caja de 12 huevos": 3000}
    producto9 ={"jamon 12 tajadas": 6000}
    producto10 ={"queso 12 tajadas": 6000}

    l.append(producto1)
    l.append(producto2)
    l.append(producto3)
    l.append(producto4)
    l.append(producto5)
    l.append(producto6)
    l.append(producto7)
    l.append(producto8)
    l.append(producto9)
    l.append(producto10)
    return render_template('form.html',lsproductos=l)

    return render_template('form.html',P1=1[0]["Gaseosa 1.5L"])
    return render_template('form.html',P2=l[1]["Gaseosa 3L"])
    return render_template('form.html',P3=l[2]["Caramelo"])
    return render_template('form.html',P4=l[3]["Leche"])
    return render_template('form.html',P5=l[4]["Papitas de pollo"])
    return render_template('form.html',P6=l[5]["DeTodito"])
    return render_template('form.html',P7=l[6]["Empanadas"])
    return render_template('form.html',P8=l[7]["Caja de 12 huevos"])
    return render_template('form.html',P9=l[8]["jamon 12 tajadas"])
    return render_template('form.html',P10=l[9]["queso 12 tajadas"])