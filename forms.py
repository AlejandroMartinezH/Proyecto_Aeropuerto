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
    nombre = StringField('nombre', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ] )

    usuario = EmailField('usuario', 
    [validators.DataRequired(message='Dato requerido.'), 
    validators.Email()])

    id_number = IntegerField('id_number', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ] )

    telefono = IntegerField('telefono', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ] )

    direccion = StringField('direccion',
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ] )

    nacimiento = DateField('nacimiento', 
    [ 
        validators.DataRequired(message='Dato requerido.'), 
    ])

    password1 = PasswordField('password1',
    [ 
        validators.DataRequired(message='Dato requerido.'), 
        validators.Length(min=8,max=25, message='Debe tener entre 8 y 25 caracteres.'),
        validators.EqualTo('confirm', message='Las Contraseñas deben coincidir')
    ])
    
    confirm = PasswordField('confirm',
    [ 
        validators.DataRequired(message='Dato requerido.'), 
        validators.Length(min=8,max=25, message='Debe tener entre 8 y 25 caracteres.'),
        validators.EqualTo('password1', message='Las Contraseñas deben coincidir')
    ])

    enviar = SubmitField('Registrar')