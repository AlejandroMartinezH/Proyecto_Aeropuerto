from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, SelectField, SubmitField, validators
from wtforms.fields.html5 import EmailField, IntegerField, DateField
import email_validator

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
    enviar = SubmitField('Ingresar')


class Formulario_registro(Form):
    nombre = StringField('Nombre', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ] )

    usuario = EmailField('Usuario', 
    [validators.DataRequired(message='Dato requerido.'), 
    validators.Email()])

    id_number = IntegerField('ID', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ] )

    telefono = IntegerField('Teléfono', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ] )

    direccion = StringField('Dirección',
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ] )

    nacimiento = DateField('Fecha Nacimiento', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ], format='%Y-%m-%d' )

    password = PasswordField('Contraseña',
    [ 
        validators.DataRequired(message='Dato requerido.'), 
        validators.Length(min=3,max=25, message='Debe tener entre 8 y 25 caracteres.'),
        validators.EqualTo('confirm', message='Las Contraseñas deben coincidir')
    ])
    
    confirm = PasswordField('Confirmar Contraseña')

    enviar = SubmitField('Registrar')
