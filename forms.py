from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, SelectField, SubmitField, validators
from wtforms.fields.html5 import EmailField

class Formulario_Usuario(Form):
    usuario = StringField('Usuario', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
        validators.Length(min=2,max=25, message='Debe tener entre 4 y 25 caracteres.')
    ] )
    password = PasswordField('Contraseña',
    [ 
        validators.DataRequired(message='Dato requerido.'), 
        validators.Length(min=3,max=25, message='Debe tener entre 8 y 25 caracteres.')
    ])
    recordar = BooleanField('Recordar usuario')
    enviar = SubmitField('Ingresar')
