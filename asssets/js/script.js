function jugar() {
    if (usuarioRegistrado()) {
        window.location.href = "juego.html"; // Redirige al juego si está registrado
    } else {
        window.location.href = "registro.html"; // Redirige al registro si no está registrado
    }
}

function usuarioRegistrado() {
    
    return false; 
}