function  validar_formulario(){
    
    vPassword = document.getElementById("password1").value;
    vPassword2 = document.getElementById("confirm").value;
    
    if ( vPassword != vPassword2 ){
        alert("Ambas contraseñas deben coincidir");
        return false;
    }
}